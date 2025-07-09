#!/usr/bin/env python3

import os
import pandas as pd
import PyPDF2
import re
from datetime import datetime
from typing import List, Dict, Optional
import io
import email

class DemoInvoiceExtractor:
    def __init__(self):
        """Initialize the Demo Invoice Extractor"""
        self.invoices_data = []
        
        # Known Paul Bandarian email files from our search
        self.known_paul_files = [
            "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox/21D02A97-B75B-4219-B77B-8F1750B76402/Data/9/0/4/Messages/409213.emlx",
            "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox/21D02A97-B75B-4219-B77B-8F1750B76402/Data/9/6/4/Messages/469497.emlx",
            "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox/21D02A97-B75B-4219-B77B-8F1750B76402/Data/9/1/4/Messages/419376.emlx",
            "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox/21D02A97-B75B-4219-B77B-8F1750B76402/Data/9/3/4/Messages/439728.emlx",
            "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox/21D02A97-B75B-4219-B77B-8F1750B76402/Data/9/3/4/Messages/439790.emlx"
        ]
        
    def process_all_invoices(self) -> pd.DataFrame:
        """Process known Paul's emails and extract invoice data"""
        print(f"🔍 Processing {len(self.known_paul_files)} known Paul Bandarian emails...")
        
        invoice_count = 0
        
        for i, email_path in enumerate(self.known_paul_files):
            print(f"\\n📧 Processing {i+1}/{len(self.known_paul_files)}: {os.path.basename(email_path)}")
            
            try:
                # Check if file exists
                if not os.path.exists(email_path):
                    print(f"  ❌ File not found")
                    continue
                
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
        
        print(f"\\n🎉 Processed {len(self.known_paul_files)} emails, found {invoice_count} invoices")
        print(f"📊 Extracted data from {len(self.invoices_data)} PDF attachments")
        
        return pd.DataFrame(self.invoices_data)
    
    def is_invoice_email(self, emlx_path: str) -> bool:
        """Check if email contains invoice attachments or invoice in subject"""
        try:
            with open(emlx_path, 'rb') as f:
                f.readline()  # Skip length
                content = f.read(4000).decode('utf-8', errors='ignore')
            
            # Look for PDF attachments in headers or invoice in subject
            has_pdf = 'application/pdf' in content.lower()
            has_invoice_subject = 'invoice' in content.lower()
            
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
            
            print(f"    📝 Subject: {subject}")
            print(f"    📅 Date: {date_str}")
            
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
                            
                            self.invoices_data.append(invoice_data)
                            
                            print(f"      💰 Amount: {invoice_data.get('amount', 'N/A')}")
                            print(f"      📅 Invoice Date: {invoice_data.get('date', 'N/A')}")
                            print(f"      🏢 Equity: {invoice_data.get('allocation_to_equity', 'N/A')}")
                            print(f"      💸 GST: {invoice_data.get('gst', 'N/A')}")
                            print(f"      📝 Description: {invoice_data.get('description', 'N/A')[:50]}...")
                            
                        else:
                            print(f"      ❌ Could not extract text from PDF {i}")
                            
                    except Exception as e:
                        print(f"      ❌ Error processing PDF {i}: {str(e)}")
            else:
                print("    📧 No PDF attachments found")
                # Still record this as an email without attachment
                invoice_data = {
                    'amount': None,
                    'allocation_to_equity': None,
                    'date': None,
                    'description': f"Email without PDF: {subject}",
                    'gst': None,
                    'email_subject': subject,
                    'email_date': date_str,
                    'email_from': from_addr,
                    'emlx_path': emlx_path,
                    'pdf_index': None
                }
                self.invoices_data.append(invoice_data)
                
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
        
        # Extract amount - Paul's invoices use "T O T A L" format
        amount_patterns = [
            r'T\s*O\s*T\s*A\s*L\s+(\d+\.?\d*)\s*\$',  # T O T A L 700.00 $
            r'TOTAL[:\s]*\$?([\d,]+\.?\d*)',
            r'Total[:\s]*\$?([\d,]+\.?\d*)',
            r'\$\s*([\d,]+\.?\d*)'
        ]
        
        for pattern in amount_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['amount'] = f"${match.group(1)}"
                break
        
        # Extract allocation to equity
        equity_patterns = [
            r'allocation to equity[:\s]*\$?([\d,]+\.?\d*)',
            r'equity[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in equity_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['allocation_to_equity'] = f"${match.group(1)}"
                break
        
        # Extract date - look for date after "David Leitch - ITK Services"
        date_patterns = [
            r'David Leitch - ITK Services\s+(\d{1,2}/\d{1,2}/\d{4})',
            r'\b(\d{1,2}/\d{1,2}/\d{4})\b',
            r'Date[:\s]*(\d{1,2}/\d{1,2}/\d{4})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['date'] = match.group(1)
                break
        
        # Extract GST
        gst_patterns = [
            r'GST[:\s]*\$?([\d,]+\.?\d*)',
            r'Tax[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in gst_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['gst'] = f"${match.group(1)}"
                break
        
        # Extract description - look for project description
        # First try to get the main service description
        description_patterns = [
            r'([^\n]*(?:REZ|Portfolio|Optimization|Analysis|System|Dispatch)[^\n]*)',
            r'D\s*E\s*S\s*C\s*R\s*I\s*P\s*T\s*I\s*O\s*N.*?\n([^\n$]+)',
        ]
        
        for pattern in description_patterns:
            matches = re.findall(pattern, pdf_text, re.IGNORECASE)
            if matches:
                # Take the first meaningful match
                desc = matches[0] if isinstance(matches[0], str) else matches[0][0] if matches[0] else ""
                if desc and len(desc.strip()) > 10:
                    desc = re.sub(r'\s+', ' ', desc.strip())
                    desc = re.sub(r'[•]+', '• ', desc)
                    invoice_data['description'] = desc[:200] + ('...' if len(desc) > 200 else '')
                    break
        
        return invoice_data

def main():
    """Main function"""
    print("🔍 Demo Invoice Extractor for Paul Bandarian")
    print("=" * 60)
    
    extractor = DemoInvoiceExtractor()
    
    try:
        # Process all invoices
        df = extractor.process_all_invoices()
        
        if df.empty:
            print("❌ No invoice data found.")
            return None
        
        # Display summary
        print(f"\\n📊 SUMMARY")
        print("=" * 60)
        print(f"Total records processed: {len(df)}")
        
        # Count invoices with amounts
        invoices_with_amounts = df[df['amount'].notna() & (df['amount'] != 'None')]['amount'].count()
        print(f"Invoices with amounts: {invoices_with_amounts}")
        
        # Show detailed results
        print(f"\\n📄 DETAILED RESULTS")
        print("=" * 60)
        
        for i, row in df.iterrows():
            print(f"\\n📧 Record {i+1}:")
            print(f"  Subject: {row.get('email_subject', 'N/A')}")
            print(f"  Amount: {row.get('amount', 'N/A')}")
            print(f"  Date: {row.get('date', 'N/A')}")
            print(f"  Equity: {row.get('allocation_to_equity', 'N/A')}")
            print(f"  GST: {row.get('gst', 'N/A')}")
            print(f"  Description: {row.get('description', 'N/A')}")
        
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