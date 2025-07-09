#!/usr/bin/env python3

import os
import pandas as pd
import PyPDF2
import re
from datetime import datetime
from typing import List, Dict, Optional
import io
import email
import subprocess

class FinalInvoiceExtractor:
    def __init__(self):
        """Initialize the Final Invoice Extractor"""
        self.invoices_data = []
        
    def find_paul_emails(self) -> List[str]:
        """Find all Paul Bandarian emails using grep"""
        print("Finding Paul Bandarian emails...")
        
        try:
            # Use grep to find files containing Paul's email
            cmd = [
                'find', 
                '/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox',
                '-name', '*.emlx',
                '-exec', 'grep', '-l', 'paul.bandarian@gmail.com', '{}', ';'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
                print(f"Found {len(files)} Paul Bandarian emails")
                return files
            else:
                print("No emails found via grep")
                return []
                
        except subprocess.TimeoutExpired:
            print("Search timed out")
            return []
        except Exception as e:
            print(f"Search error: {str(e)}")
            return []
    
    def process_all_invoices(self) -> pd.DataFrame:
        """Process all Paul's emails and extract invoice data"""
        paul_emails = self.find_paul_emails()
        
        if not paul_emails:
            print("No Paul Bandarian emails found")
            return pd.DataFrame()
        
        invoice_count = 0
        processed_count = 0
        
        for email_path in paul_emails:
            processed_count += 1
            print(f"\\nProcessing {processed_count}/{len(paul_emails)}: {os.path.basename(email_path)}")
            
            try:
                # Check if this is an invoice email
                if self.is_invoice_email(email_path):
                    invoice_count += 1
                    print(f"  📄 Invoice email #{invoice_count}")
                    self.process_invoice_email(email_path)
                else:
                    print("  ✉️  Regular email (no invoice)")
                    
            except Exception as e:
                print(f"  ❌ Error: {str(e)}")
                continue
        
        print(f"\\n🎉 Processed {processed_count} emails, found {invoice_count} invoices")
        print(f"📊 Extracted data from {len(self.invoices_data)} PDF attachments")
        
        return pd.DataFrame(self.invoices_data)
    
    def is_invoice_email(self, emlx_path: str) -> bool:
        """Check if email contains invoice attachments"""
        try:
            with open(emlx_path, 'rb') as f:
                f.readline()  # Skip length
                content = f.read(4000).decode('utf-8', errors='ignore')
            
            # Look for PDF attachments in headers
            has_pdf = 'application/pdf' in content.lower()
            has_invoice_subject = ('invoice' in content.lower() and 
                                 'subject: re:' not in content.lower())
            
            return has_pdf or has_invoice_subject
            
        except Exception:
            return False
    
    def process_invoice_email(self, emlx_path: str):
        """Process a single invoice email"""
        try:
            with open(emlx_path, 'rb') as f:
                f.readline()  # Skip length
                email_content = f.read()
            
            # Parse email
            msg = email.message_from_bytes(email_content)
            
            # Extract basic info
            subject = msg.get('Subject', 'Unknown')
            date_str = msg.get('Date', 'Unknown')
            from_addr = msg.get('From', 'Unknown')
            
            print(f"    Subject: {subject}")
            print(f"    From: {from_addr}")
            print(f"    Date: {date_str}")
            
            # Extract PDF attachments
            pdf_attachments = self.extract_pdf_attachments(msg)
            
            if pdf_attachments:
                print(f"    📎 Found {len(pdf_attachments)} PDF attachment(s)")
                
                for i, pdf_data in enumerate(pdf_attachments):
                    try:
                        # Extract text from PDF
                        pdf_text = self.extract_text_from_pdf(pdf_data)
                        
                        if pdf_text and len(pdf_text) > 50:  # Valid PDF with content
                            # Parse invoice data
                            invoice_data = self.parse_invoice_data(pdf_text)
                            invoice_data['email_subject'] = subject
                            invoice_data['email_date'] = date_str
                            invoice_data['email_from'] = from_addr
                            invoice_data['emlx_path'] = emlx_path
                            invoice_data['pdf_index'] = i
                            invoice_data['pdf_text_sample'] = pdf_text[:200] + '...'
                            
                            self.invoices_data.append(invoice_data)
                            
                            print(f"      💰 Amount: {invoice_data.get('amount', 'N/A')}")
                            print(f"      📅 Date: {invoice_data.get('date', 'N/A')}")
                            print(f"      📝 Description: {invoice_data.get('description', 'N/A')}")
                            
                        else:
                            print(f"      ❌ Could not extract text from PDF {i}")
                            
                    except Exception as e:
                        print(f"      ❌ Error processing PDF {i}: {str(e)}")
            else:
                print("    📧 No PDF attachments found")
                
        except Exception as e:
            print(f"    ❌ Error processing email: {str(e)}")
    
    def extract_pdf_attachments(self, msg) -> List[bytes]:
        """Extract PDF attachments from email message"""
        pdf_attachments = []
        
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename()
                if filename and filename.lower().endswith('.pdf'):
                    pdf_data = part.get_payload(decode=True)
                    if pdf_data:
                        pdf_attachments.append(pdf_data)
        
        return pdf_attachments
    
    def extract_text_from_pdf(self, pdf_data: bytes) -> str:
        """Extract text content from PDF bytes"""
        try:
            pdf_file = io.BytesIO(pdf_data)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            return text
        except Exception as e:
            raise Exception(f"PDF extraction failed: {str(e)}")
    
    def parse_invoice_data(self, pdf_text: str) -> Dict[str, Optional[str]]:
        """Parse invoice data from PDF text"""
        invoice_data = {
            'amount': None,
            'allocation_to_equity': None,
            'date': None,
            'description': None,
            'gst': None
        }
        
        # Extract amount - look for T O T A L pattern specific to Paul's invoices
        amount_patterns = [
            r'T\\s*O\\s*T\\s*A\\s*L\\s+(\\d+\\.?\\d*)\\s*\\$',  # Paul's format: T O T A L 700.00 $
            r'TOTAL[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'Total[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'Amount[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'Invoice Total[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'\\$\\s*([\\d,]+\\.?\\d*)'
        ]
        
        for pattern in amount_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['amount'] = f"${match.group(1)}"
                break
        
        # Extract allocation to equity
        equity_patterns = [
            r'allocation to equity[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'equity allocation[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'equity[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'share[:\\s]*\\$?([\\d,]+\\.?\\d*)'
        ]
        
        for pattern in equity_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['allocation_to_equity'] = f"${match.group(1)}"
                break
        
        # Extract date
        date_patterns = [
            r'David Leitch - ITK Services\\s+(\\d{1,2}/\\d{1,2}/\\d{4})',  # Paul's format
            r'\\b(\\d{1,2}/\\d{1,2}/\\d{4})\\b',
            r'\\b(\\d{1,2}-\\d{1,2}-\\d{4})\\b',
            r'Date[:\\s]*(\\d{1,2}[/\\-]\\d{1,2}[/\\-]\\d{2,4})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['date'] = match.group(1)
                break
        
        # Extract GST
        gst_patterns = [
            r'GST[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'VAT[:\\s]*\\$?([\\d,]+\\.?\\d*)',
            r'Tax[:\\s]*\\$?([\\d,]+\\.?\\d*)'
        ]
        
        for pattern in gst_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['gst'] = f"${match.group(1)}"
                break
        
        # Extract description
        description_patterns = [
            r'D\\s*E\\s*S\\s*C\\s*R\\s*I\\s*P\\s*T\\s*I\\s*O\\s*N.*?\\n([^$\\n]+)',  # Paul's format
            r'Description[:\\s]*([^\\n\\r]{10,200})',
            r'Project[:\\s]*([^\\n\\r]{10,200})'
        ]
        
        for pattern in description_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE | re.DOTALL)
            if match:
                desc = match.group(1).strip()
                desc = re.sub(r'\\s+', ' ', desc)
                desc = re.sub(r'[•]+', '• ', desc)
                invoice_data['description'] = desc[:200] + ('...' if len(desc) > 200 else '')
                break
        
        # Fallback description
        if not invoice_data['description']:
            lines = pdf_text.split('\\n')
            for line in lines:
                line = line.strip()
                if any(keyword in line.lower() for keyword in ['rez', 'optimiz', 'portfolio', 'analysis', 'system', 'dispatch', 'consulting', 'service']) and len(line) > 15:
                    desc = re.sub(r'\\s+', ' ', line)
                    invoice_data['description'] = desc[:200] + ('...' if len(desc) > 200 else '')
                    break
        
        return invoice_data

def main():
    """Main function"""
    print("🔍 Final Invoice Extractor for Paul Bandarian emails")
    print("=" * 60)
    
    extractor = FinalInvoiceExtractor()
    
    try:
        # Process all invoices
        df = extractor.process_all_invoices()
        
        if df.empty:
            print("❌ No invoice data found.")
            return None
        
        # Display summary
        print(f"\\n📊 SUMMARY")
        print("=" * 60)
        print(f"Total invoices processed: {len(df)}")
        
        if 'amount' in df.columns:
            amounts = [amt for amt in df['amount'] if amt and amt != 'None']
            if amounts:
                print(f"Total amount found: {len(amounts)} invoices")
        
        # Show detailed results
        print(f"\\n📄 DETAILED RESULTS")
        print("=" * 60)
        
        for i, row in df.iterrows():
            print(f"\\nInvoice {i+1}:")
            print(f"  📧 Subject: {row.get('email_subject', 'N/A')}")
            print(f"  💰 Amount: {row.get('amount', 'N/A')}")
            print(f"  📅 Date: {row.get('date', 'N/A')}")
            print(f"  🏢 Equity: {row.get('allocation_to_equity', 'N/A')}")
            print(f"  💸 GST: {row.get('gst', 'N/A')}")
            print(f"  📝 Description: {row.get('description', 'N/A')}")
            print(f"  📁 File: {os.path.basename(row.get('emlx_path', 'N/A'))}")
        
        # Save to CSV
        output_file = f"paul_bandarian_invoices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\\n💾 Data saved to: {output_file}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

if __name__ == "__main__":
    df = main()