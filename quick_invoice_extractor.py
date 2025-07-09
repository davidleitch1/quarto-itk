#!/usr/bin/env python3

import os
import pandas as pd
import PyPDF2
import re
from datetime import datetime
from typing import List, Dict, Optional
import io
import email
import base64

class QuickInvoiceExtractor:
    def __init__(self):
        """Initialize the Quick Invoice Extractor"""
        self.invoices_data = []
        self.mail_data_path = os.path.expanduser("~/Library/Mail/V10")
        self.processed_count = 0
        self.max_emails_to_process = 50  # Limit for testing
        
    def find_paul_bandarian_invoices(self) -> pd.DataFrame:
        """Find and process Paul Bandarian invoice emails efficiently"""
        print("Searching for Paul Bandarian invoice emails...")
        
        # Target the most likely mailbox - INBOX
        target_mbox = "/Users/davidleitch/Library/Mail/V10/777F3AD8-D879-4617-BC00-1C20B16A4EAA/INBOX.mbox"
        
        if not os.path.exists(target_mbox):
            print(f"Target mailbox not found: {target_mbox}")
            return pd.DataFrame()
        
        print(f"Searching in: {target_mbox}")
        
        # Walk through the Data directory structure
        data_path = os.path.join(target_mbox, "21D02A97-B75B-4219-B77B-8F1750B76402", "Data")
        
        if not os.path.exists(data_path):
            print(f"Data directory not found: {data_path}")
            return pd.DataFrame()
        
        # Process .emlx files
        for root, dirs, files in os.walk(data_path):
            if self.processed_count >= self.max_emails_to_process:
                print(f"Reached processing limit of {self.max_emails_to_process} emails")
                break
                
            for file in files:
                if file.endswith('.emlx'):
                    emlx_path = os.path.join(root, file)
                    
                    try:
                        if self.is_paul_bandarian_invoice(emlx_path):
                            print(f"Processing: {emlx_path}")
                            self.process_invoice_email(emlx_path)
                            self.processed_count += 1
                            
                            if self.processed_count >= self.max_emails_to_process:
                                break
                                
                    except Exception as e:
                        # Skip problematic files
                        continue
        
        print(f"Processed {len(self.invoices_data)} invoice emails")
        return pd.DataFrame(self.invoices_data)
    
    def is_paul_bandarian_invoice(self, emlx_path: str) -> bool:
        """Quick check if email is from Paul Bandarian with Invoice (not a reply)"""
        try:
            with open(emlx_path, 'rb') as f:
                # Skip the first line (message length)
                f.readline()
                # Read first 2000 bytes to check headers
                header_content = f.read(2000).decode('utf-8', errors='ignore').lower()
            
            # Must be from Paul Bandarian, contain "invoice", but NOT be a reply
            return ('paul.bandarian@gmail.com' in header_content and 
                    'invoice' in header_content and
                    'subject: re:' not in header_content and
                    'subject: fwd:' not in header_content)
                    
        except Exception:
            return False
    
    def process_invoice_email(self, emlx_path: str):
        """Process a single invoice email"""
        try:
            with open(emlx_path, 'rb') as f:
                # Skip the first line (message length)
                f.readline()
                email_content = f.read()
            
            # Parse email
            msg = email.message_from_bytes(email_content)
            
            # Extract basic info
            subject = msg.get('Subject', 'Unknown')
            date_str = msg.get('Date', 'Unknown')
            
            print(f"  Subject: {subject}")
            print(f"  Date: {date_str}")
            
            # Extract PDF attachments
            pdf_attachments = self.extract_pdf_attachments(msg)
            
            if pdf_attachments:
                print(f"  Found {len(pdf_attachments)} PDF attachment(s)")
                
                for i, pdf_data in enumerate(pdf_attachments):
                    try:
                        # Extract text from PDF
                        pdf_text = self.extract_text_from_pdf(pdf_data)
                        
                        if pdf_text:
                            # Parse invoice data
                            invoice_data = self.parse_invoice_data(pdf_text)
                            invoice_data['email_subject'] = subject
                            invoice_data['email_date'] = date_str
                            invoice_data['emlx_path'] = emlx_path
                            invoice_data['pdf_index'] = i
                            
                            self.invoices_data.append(invoice_data)
                            
                            print(f"    Extracted: Amount={invoice_data.get('amount')}, "
                                  f"Date={invoice_data.get('date')}")
                        else:
                            print(f"    Could not extract text from PDF {i}")
                            
                    except Exception as e:
                        print(f"    Error processing PDF {i}: {str(e)}")
            else:
                print("  No PDF attachments found")
                
        except Exception as e:
            print(f"Error processing email {emlx_path}: {str(e)}")
    
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
            print(f"    PDF extraction error: {str(e)}")
            return ""
    
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
            r'T\s*O\s*T\s*A\s*L\s+(\d+\.?\d*)\s*\$',  # Paul's format: T O T A L 700.00 $
            r'TOTAL[:\s]*\$?([\d,]+\.?\d*)',
            r'Total[:\s]*\$?([\d,]+\.?\d*)',
            r'Amount[:\s]*\$?([\d,]+\.?\d*)',
            r'Invoice Total[:\s]*\$?([\d,]+\.?\d*)',
            r'\$\s*([\d,]+\.?\d*)'
        ]
        
        for pattern in amount_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['amount'] = f"${match.group(1)}"
                break
        
        # Extract allocation to equity - search for equity-related terms
        equity_patterns = [
            r'allocation to equity[:\s]*\$?([\d,]+\.?\d*)',
            r'equity allocation[:\s]*\$?([\d,]+\.?\d*)',
            r'equity[:\s]*\$?([\d,]+\.?\d*)',
            r'share[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in equity_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['allocation_to_equity'] = f"${match.group(1)}"
                break
        
        # Extract date - multiple date formats, prioritize the one after "David Leitch - ITK Services"
        date_patterns = [
            r'David Leitch - ITK Services\s+(\d{1,2}/\d{1,2}/\d{4})',  # Paul's format
            r'\b(\d{1,2}/\d{1,2}/\d{4})\b',
            r'\b(\d{1,2}-\d{1,2}-\d{4})\b',
            r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{2,4})\b',
            r'Date[:\s]*(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})',
            r'Invoice Date[:\s]*(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['date'] = match.group(1)
                break
        
        # Extract GST - look for various tax patterns
        gst_patterns = [
            r'GST[:\s]*\$?([\d,]+\.?\d*)',
            r'VAT[:\s]*\$?([\d,]+\.?\d*)',
            r'Tax[:\s]*\$?([\d,]+\.?\d*)',
            r'HST[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in gst_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['gst'] = f"${match.group(1)}"
                break
        
        # Extract description - look for the project description after D E S C R I P T I O N
        description_patterns = [
            r'D\s*E\s*S\s*C\s*R\s*I\s*P\s*T\s*I\s*O\s*N.*?\n([^$\n]+)',  # Paul's format
            r'Description[:\s]*([^\n\r]{10,200})',
            r'Services?[:\s]*([^\n\r]{10,200})',
            r'For[:\s]*([^\n\r]{10,200})',
            r'Project[:\s]*([^\n\r]{10,200})'
        ]
        
        for pattern in description_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE | re.DOTALL)
            if match:
                desc = match.group(1).strip()
                # Clean up the description
                desc = re.sub(r'\s+', ' ', desc)
                desc = re.sub(r'[•]+', '• ', desc)  # Clean up bullet points
                invoice_data['description'] = desc[:200] + ('...' if len(desc) > 200 else '')
                break
        
        # Fallback: look for project names or meaningful content
        if not invoice_data['description']:
            # Look for lines that contain project-related keywords
            lines = pdf_text.split('\n')
            for line in lines:
                line = line.strip()
                if any(keyword in line.lower() for keyword in ['rez', 'optimiz', 'portfolio', 'analysis', 'system', 'dispatch']) and len(line) > 15:
                    desc = re.sub(r'\s+', ' ', line)
                    invoice_data['description'] = desc[:200] + ('...' if len(desc) > 200 else '')
                    break
        
        return invoice_data

def main():
    """Main function"""
    print("Quick Invoice Extractor for Paul Bandarian emails")
    print("=" * 50)
    
    extractor = QuickInvoiceExtractor()
    
    try:
        # Process invoices
        df = extractor.find_paul_bandarian_invoices()
        
        if df.empty:
            print("No invoice data found.")
            return None
        
        # Display results
        print(f"\nExtracted {len(df)} invoices:")
        print("=" * 50)
        
        # Show summary
        for i, row in df.iterrows():
            print(f"\nInvoice {i+1}:")
            print(f"  Subject: {row.get('email_subject', 'N/A')}")
            print(f"  Amount: {row.get('amount', 'N/A')}")
            print(f"  Date: {row.get('date', 'N/A')}")
            print(f"  Equity: {row.get('allocation_to_equity', 'N/A')}")
            print(f"  GST: {row.get('gst', 'N/A')}")
            print(f"  Description: {row.get('description', 'N/A')}")
        
        # Save to CSV
        output_file = f"paul_bandarian_invoices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\nData saved to: {output_file}")
        
        return df
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    df = main()