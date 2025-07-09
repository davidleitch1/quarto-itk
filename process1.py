#!/usr/bin/env python3

import os
import json
import glob
import pandas as pd
from datetime import datetime
from email.message import EmailMessage
from email import message_from_bytes
from typing import Dict, Optional, List
import time

class BatchClaudeInvoiceExtractor:
    def __init__(self):
        """Extract invoice data from all Bandarian emails using Claude API"""
        self.mail_path = os.path.expanduser("~/Library/Mail")
        self.found_emails = []
        self.processed_invoices = []
        
        # Check for Claude API key
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            print("⚠️  ANTHROPIC_API_KEY environment variable not set")
            return
        
        # Check libraries
        try:
            import fitz  # PyMuPDF
            self.fitz = fitz
            print("✅ Found PyMuPDF library")
        except ImportError:
            print("❌ PyMuPDF library not found. Install with: pip install PyMuPDF")
            self.fitz = None
            return
        
        try:
            import anthropic
            self.anthropic = anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
            print("✅ Found Anthropic library and API key")
        except ImportError:
            print("❌ Anthropic library not found. Install with: pip install anthropic")
            self.anthropic = None
            self.client = None
            return
        
        try:
            import emlx
            self.emlx = emlx
            print("✅ Found emlx library")
        except ImportError:
            print("❌ emlx library not found. Install with: pip install emlx")
            self.emlx = None
    
    def find_all_bandarian_emails(self) -> List[Dict]:
        """Find all emails from paul.bandarian@gmail.com with 'invoice' in subject"""
        print("🔍 Finding all Paul Bandarian invoice emails...")
        
        # Use glob to find all .emlx files recursively
        pattern = os.path.join(self.mail_path, "**", "*.emlx")
        emlx_files = glob.glob(pattern, recursive=True)
        
        print(f"📧 Found {len(emlx_files)} total .emlx files")
        
        bandarian_invoices = []
        processed = 0
        
        for filepath in emlx_files:
            processed += 1
            
            # Progress indicator every 1000 files
            if processed % 1000 == 0:
                print(f"  📊 Processed {processed}/{len(emlx_files)} files...")
            
            try:
                # Parse the emlx file
                if self.emlx:
                    message = self.emlx.read(filepath)
                    from_header = message.headers.get('From', '').lower()
                    subject = message.headers.get('Subject', '').lower()
                else:
                    # Fallback to manual parsing
                    with open(filepath, 'rb') as f:
                        f.readline()  # Skip length
                        email_content = f.read()
                    
                    msg = message_from_bytes(email_content)
                    from_header = msg.get('From', '').lower()
                    subject = msg.get('Subject', '').lower()
                    
                    # Create message-like object for consistency
                    class SimpleMessage:
                        def __init__(self, msg):
                            self.headers = {k: v for k, v in msg.items()}
                    message = SimpleMessage(msg)
                
                # Check if it's from Paul Bandarian with invoice in subject
                if 'paul.bandarian@gmail.com' not in from_header:
                    continue
                
                if 'invoice' not in subject:
                    continue
                
                # This is a Paul Bandarian invoice email!
                email_data = {
                    'filepath': filepath,
                    'from': message.headers.get('From', ''),
                    'subject': message.headers.get('Subject', ''),
                    'date': message.headers.get('Date', ''),
                    'message_id': message.headers.get('Message-ID', ''),
                }
                
                bandarian_invoices.append(email_data)
                
            except Exception as e:
                # Skip files that can't be read
                continue
        
        print(f"\n🎯 Found {len(bandarian_invoices)} Paul Bandarian invoice emails")
        return bandarian_invoices
    
    def read_emlx_raw(self, filepath: str) -> EmailMessage:
        """Read .emlx file using raw email parsing"""
        try:
            with open(filepath, 'rb') as f:
                f.readline()  # Skip length
                email_content = f.read()
            
            msg = message_from_bytes(email_content)
            return msg
            
        except Exception as e:
            print(f"❌ Error reading {filepath}: {str(e)}")
            return None
    
    def find_pdf_attachments(self, msg: EmailMessage) -> List[bytes]:
        """Extract PDF attachments from email message"""
        pdf_attachments = []
        
        for part in msg.walk():
            content_type = part.get_content_type()
            filename = part.get_filename()
            
            if content_type == 'application/pdf' or (filename and filename.lower().endswith('.pdf')):
                pdf_data = part.get_payload(decode=True)
                if pdf_data and len(pdf_data) > 1000:
                    pdf_attachments.append(pdf_data)
        
        return pdf_attachments
    
    def extract_text_with_pymupdf(self, pdf_data: bytes) -> str:
        """Extract text using PyMuPDF"""
        try:
            doc = self.fitz.open(stream=pdf_data, filetype="pdf")
            text = doc[0].get_text()
            doc.close()
            return text
        except Exception as e:
            return ""
    
    def create_extraction_prompt(self, pdf_text: str) -> str:
        """Create a structured prompt for Claude to extract invoice data"""
        prompt = f"""I need you to extract specific information from this invoice text. Please analyze the text and return ONLY a valid JSON object with the following fields:

{{
  "invoice_number": "The invoice number (e.g., ITK2519)",
  "invoice_date": "The invoice date in format DD/MM/YYYY",
  "amount": "The total amount as a number (e.g., 3560.00)",
  "gst": "The GST amount as a number (e.g., 360.00)",
  "allocation_to_equity": "The allocation to equity as a negative number (e.g., -400.00)",
  "description": "A brief summary of the work items/services provided"
}}

Important notes:
- Return amounts as numbers only (no $ symbols)
- For allocation_to_equity, include the negative sign if it's a negative allocation
- For description, summarize the main work items in 1-2 sentences
- If a field cannot be found, use null

Here is the invoice text:

{pdf_text}

Please return only the JSON object, no other text or explanation."""
        
        return prompt
    
    def extract_with_claude(self, pdf_text: str) -> Dict:
        """Extract invoice data using Claude API"""
        try:
            prompt = self.create_extraction_prompt(pdf_text)
            
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            response_text = response.content[0].text.strip()
            
            try:
                invoice_data = json.loads(response_text)
                return invoice_data
            except json.JSONDecodeError:
                return {}
                
        except Exception as e:
            print(f"❌ Claude API error: {str(e)}")
            return {}
    
    def format_invoice_data(self, raw_data: Dict, email_info: Dict) -> Dict:
        """Format the extracted data for DataFrame"""
        formatted = {
            'email_filepath': email_info['filepath'],
            'email_subject': email_info['subject'],
            'email_from': email_info['from'],
            'email_date': email_info['date'],
            'invoice_number': raw_data.get('invoice_number'),
            'invoice_date': raw_data.get('invoice_date'),
            'amount': raw_data.get('amount'),
            'gst': raw_data.get('gst'),
            'allocation_to_equity': raw_data.get('allocation_to_equity'),
            'description': raw_data.get('description'),
            'extraction_timestamp': datetime.now().isoformat()
        }
        
        return formatted
    
    def process_all_invoices(self):
        """Process all Bandarian invoices and extract data"""
        print("🔍 Starting batch processing of all Paul Bandarian invoices")
        print("=" * 60)
        
        if not self.client:
            print("❌ Claude API not available")
            return None
        
        # Find all emails
        emails = self.find_all_bandarian_emails()
        
        if not emails:
            print("❌ No invoice emails found")
            return None
        
        print(f"\n📧 Processing {len(emails)} invoice emails...")
        
        results = []
        processed_count = 0
        success_count = 0
        error_count = 0
        
        for i, email_info in enumerate(emails, 1):
            print(f"\n📧 Processing email {i}/{len(emails)}: {os.path.basename(email_info['filepath'])}")
            print(f"   Subject: {email_info['subject']}")
            
            try:
                # Read the email
                msg = self.read_emlx_raw(email_info['filepath'])
                if not msg:
                    error_count += 1
                    continue
                
                # Find PDF attachments
                pdf_attachments = self.find_pdf_attachments(msg)
                
                if not pdf_attachments:
                    print("   ⚠️  No PDF attachments found")
                    # Still add record with email info only
                    formatted_data = self.format_invoice_data({}, email_info)
                    results.append(formatted_data)
                    processed_count += 1
                    continue
                
                # Process first PDF attachment
                pdf_data = pdf_attachments[0]
                print(f"   📄 Found PDF ({len(pdf_data)} bytes)")
                
                # Extract text
                text = self.extract_text_with_pymupdf(pdf_data)
                if not text:
                    print("   ❌ Could not extract text from PDF")
                    error_count += 1
                    continue
                
                print(f"   📝 Extracted {len(text)} characters")
                
                # Extract with Claude
                raw_data = self.extract_with_claude(text)
                
                if raw_data:
                    print(f"   ✅ Claude extracted: {raw_data.get('invoice_number', 'N/A')}")
                    success_count += 1
                else:
                    print("   ⚠️  Claude extraction failed")
                
                # Format and add to results
                formatted_data = self.format_invoice_data(raw_data, email_info)
                results.append(formatted_data)
                processed_count += 1
                
                # Add small delay to avoid rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                print(f"   ❌ Error processing email: {str(e)}")
                error_count += 1
                continue
        
        print(f"\n🎉 BATCH PROCESSING COMPLETE!")
        print(f"  📊 Total emails: {len(emails)}")
        print(f"  ✅ Processed: {processed_count}")
        print(f"  🎯 Successful extractions: {success_count}")
        print(f"  ❌ Errors: {error_count}")
        
        # Create DataFrame
        if results:
            df = pd.DataFrame(results)
            print(f"\n📋 Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
            
            # Save to CSV
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"bandarian_invoices_{timestamp}.csv"
            df.to_csv(filename, index=False)
            print(f"💾 Saved to: {filename}")
            
            # Display summary
            print(f"\n📊 SUMMARY STATISTICS:")
            print(f"  📋 Invoices with numbers: {df['invoice_number'].notna().sum()}")
            print(f"  💰 Invoices with amounts: {df['amount'].notna().sum()}")
            print(f"  📅 Date range: {df['invoice_date'].min()} to {df['invoice_date'].max()}")
            
            if df['amount'].notna().any():
                total_amount = df['amount'].sum()
                print(f"  💵 Total amount: ${total_amount:,.2f}")
            
            return df
        
        return None

def main():
    """Main function"""
    extractor = BatchClaudeInvoiceExtractor()
    
    print("🎯 Batch Processing All Paul Bandarian Invoices")
    print("🤖 Using Claude AI for data extraction")
    print("=" * 60)
    
    if not extractor.client:
        print("❌ Setup required:")
        print("1. Get API key from: https://console.anthropic.com/")
        print("2. Set: export ANTHROPIC_API_KEY='your-key-here'")
        print("3. Install: pip install anthropic")
        return
    
    # Process all invoices
    df = extractor.process_all_invoices()
    
    if df is not None:
        print(f"\n✨ SUCCESS! Processed all invoices and saved to CSV")
        print(f"📋 DataFrame shape: {df.shape}")
        
        # Show first few rows
        print(f"\n📄 First 3 invoices:")
        for i, row in df.head(3).iterrows():
            print(f"  {i+1}. {row.get('invoice_number', 'N/A')} - {row.get('amount', 'N/A')} - {row.get('invoice_date', 'N/A')}")
    else:
        print("❌ No data processed")

if __name__ == "__main__":
    main()