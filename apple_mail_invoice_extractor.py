import os
import sqlite3
import pandas as pd
import PyPDF2
import re
from datetime import datetime
from typing import List, Dict, Optional
import io
import email
from email.mime.multipart import MIMEMultipart

class AppleMailInvoiceExtractor:
    def __init__(self):
        """Initialize the Apple Mail Invoice Extractor"""
        self.invoices_data = []
        self.mail_data_path = os.path.expanduser("~/Library/Mail/V10")
        self.envelope_db_path = os.path.join(self.mail_data_path, "MailData", "Envelope Index")
        
    def search_emails_in_database(self) -> List[Dict]:
        """Search for emails from Paul Bandarian with Invoice in subject using SQLite"""
        try:
            if not os.path.exists(self.envelope_db_path):
                print(f"Envelope Index not found at {self.envelope_db_path}")
                return []
            
            conn = sqlite3.connect(self.envelope_db_path)
            cursor = conn.cursor()
            
            # First, let's examine the database structure
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"Available tables: {tables}")
            
            # Get schema for messages table
            cursor.execute("PRAGMA table_info(messages);")
            columns = cursor.fetchall()
            print(f"Messages table columns: {columns}")
            
            # Query to find emails from Paul Bandarian with Invoice in subject
            # Updated query based on actual Apple Mail database structure
            query = """
            SELECT m.ROWID, a.address as sender, m.subject, m.date_sent, m.remote_id, m.mailbox
            FROM messages m
            JOIN addresses a ON m.sender = a.ROWID
            WHERE a.address LIKE '%paul.bandarian@gmail.com%' 
            AND m.subject LIKE '%Invoice%'
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            emails = []
            for row in results:
                emails.append({
                    'rowid': row[0],
                    'sender': row[1],
                    'subject': row[2],
                    'date_sent': row[3],
                    'remote_id': row[4],
                    'mailbox': row[5]
                })
            
            conn.close()
            return emails
            
        except Exception as e:
            print(f"Error searching database: {str(e)}")
            # Fallback: try simpler query if JOIN fails
            try:
                conn = sqlite3.connect(self.envelope_db_path)
                cursor = conn.cursor()
                
                # Simple query without JOIN
                query = """
                SELECT ROWID, sender, subject, date_sent, remote_id, mailbox
                FROM messages 
                WHERE subject LIKE '%Invoice%'
                """
                
                cursor.execute(query)
                results = cursor.fetchall()
                
                emails = []
                for row in results:
                    emails.append({
                        'rowid': row[0],
                        'sender': row[1],
                        'subject': row[2],
                        'date_sent': row[3],
                        'remote_id': row[4],
                        'mailbox': row[5]
                    })
                
                conn.close()
                return emails
                
            except Exception as e2:
                print(f"Fallback query also failed: {str(e2)}")
                return []
    
    def find_mbox_file(self, mailbox_id: int) -> Optional[str]:
        """Find the .mbox directory for a given mailbox ID"""
        try:
            # Search through account directories for the correct mailbox
            for account_dir in os.listdir(self.mail_data_path):
                if account_dir == "MailData":
                    continue
                    
                account_path = os.path.join(self.mail_data_path, account_dir)
                if not os.path.isdir(account_path):
                    continue
                
                # Look for INBOX.mbox, Archive.mbox, etc.
                for mbox_name in os.listdir(account_path):
                    if mbox_name.endswith('.mbox'):
                        mbox_path = os.path.join(account_path, mbox_name)
                        # Check if this mbox contains our target emails
                        if os.path.exists(mbox_path):
                            return mbox_path
            
            return None
        except Exception as e:
            print(f"Error finding mbox file: {str(e)}")
            return None
    
    def find_emlx_files_in_mbox(self, mbox_path: str) -> List[str]:
        """Find all .emlx files in a .mbox directory"""
        try:
            emlx_files = []
            
            # The structure is: mbox_path/UUID/Data/X/Y/Z/Messages/*.emlx
            for item in os.listdir(mbox_path):
                if item == "Info.plist":
                    continue
                    
                uuid_path = os.path.join(mbox_path, item)
                if not os.path.isdir(uuid_path):
                    continue
                
                data_path = os.path.join(uuid_path, "Data")
                if not os.path.exists(data_path):
                    continue
                
                # Recursively search through the Data directory structure
                for root, dirs, files in os.walk(data_path):
                    for file in files:
                        if file.endswith('.emlx'):
                            emlx_files.append(os.path.join(root, file))
            
            return emlx_files
        except Exception as e:
            print(f"Error finding emlx files: {str(e)}")
            return []
    
    def extract_attachments_from_emlx(self, emlx_path: str) -> List[bytes]:
        """Extract PDF attachments from .emlx file"""
        try:
            with open(emlx_path, 'rb') as f:
                # Skip the first line which contains the message length
                f.readline()
                email_content = f.read()
            
            # Parse as email message
            import email
            msg = email.message_from_bytes(email_content)
            
            pdf_attachments = []
            for part in msg.walk():
                if part.get_content_disposition() == 'attachment':
                    filename = part.get_filename()
                    if filename and filename.lower().endswith('.pdf'):
                        pdf_data = part.get_payload(decode=True)
                        pdf_attachments.append(pdf_data)
            
            return pdf_attachments
            
        except Exception as e:
            print(f"Error extracting attachments: {str(e)}")
            return []
    
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
            print(f"Error extracting PDF text: {str(e)}")
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
        
        # Extract amount - look for currency patterns
        amount_patterns = [
            r'\$[\d,]+\.?\d*',
            r'Total[:\s]*\$?([\d,]+\.?\d*)',
            r'Amount[:\s]*\$?([\d,]+\.?\d*)',
            r'Invoice Total[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in amount_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['amount'] = match.group(0) if '$' in match.group(0) else f"${match.group(1)}"
                break
        
        # Extract allocation to equity
        equity_patterns = [
            r'allocation to equity[:\s]*\$?([\d,]+\.?\d*)',
            r'equity allocation[:\s]*\$?([\d,]+\.?\d*)',
            r'equity[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in equity_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['allocation_to_equity'] = f"${match.group(1)}"
                break
        
        # Extract date - multiple date formats
        date_patterns = [
            r'\b(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})\b',
            r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{2,4})\b',
            r'Date[:\s]*(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})',
            r'Invoice Date[:\s]*(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4})'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['date'] = match.group(1)
                break
        
        # Extract GST
        gst_patterns = [
            r'GST[:\s]*\$?([\d,]+\.?\d*)',
            r'VAT[:\s]*\$?([\d,]+\.?\d*)',
            r'Tax[:\s]*\$?([\d,]+\.?\d*)'
        ]
        
        for pattern in gst_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                invoice_data['gst'] = f"${match.group(1)}"
                break
        
        # Extract description - first meaningful sentence or line item
        description_patterns = [
            r'Description[:\s]*([^\n\r]{10,100})',
            r'Services?[:\s]*([^\n\r]{10,100})',
            r'For[:\s]*([^\n\r]{10,100})'
        ]
        
        for pattern in description_patterns:
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                desc = match.group(1).strip()
                desc = re.sub(r'\s+', ' ', desc)
                invoice_data['description'] = desc[:100] + ('...' if len(desc) > 100 else '')
                break
        
        # Fallback: get first meaningful line as description
        if not invoice_data['description']:
            lines = pdf_text.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) > 20 and not re.match(r'^[\d\s\$\.,]+$', line):
                    invoice_data['description'] = line[:100] + ('...' if len(line) > 100 else '')
                    break
        
        return invoice_data
    
    def process_all_invoices(self) -> pd.DataFrame:
        """Process all invoice emails and return DataFrame"""
        print("Searching for invoice emails in Apple Mail database...")
        emails = self.search_emails_in_database()
        print(f"Found {len(emails)} invoice emails")
        
        if not emails:
            print("No invoice emails found. Let's search all .emlx files for Paul Bandarian emails with Invoice in subject...")
            return self.fallback_search_emlx_files()
        
        for i, email_info in enumerate(emails):
            print(f"Processing email {i+1}/{len(emails)}: {email_info.get('subject', 'Unknown subject')}")
            
            try:
                # Find mbox files and search for relevant emails
                mbox_paths = []
                for account_dir in os.listdir(self.mail_data_path):
                    if account_dir == "MailData":
                        continue
                    account_path = os.path.join(self.mail_data_path, account_dir)
                    if os.path.isdir(account_path):
                        for mbox_name in os.listdir(account_path):
                            if mbox_name.endswith('.mbox'):
                                mbox_paths.append(os.path.join(account_path, mbox_name))
                
                # Search all mbox directories for .emlx files
                found_match = False
                for mbox_path in mbox_paths:
                    emlx_files = self.find_emlx_files_in_mbox(mbox_path)
                    
                    for emlx_path in emlx_files:
                        if self.check_emlx_matches_criteria(emlx_path, email_info):
                            # Extract PDFs from email
                            pdf_attachments = self.extract_attachments_from_emlx(emlx_path)
                            
                            for pdf_data in pdf_attachments:
                                # Extract text from PDF
                                pdf_text = self.extract_text_from_pdf(pdf_data)
                                
                                # Parse invoice data
                                invoice_data = self.parse_invoice_data(pdf_text)
                                invoice_data['email_subject'] = email_info.get('subject', 'Unknown')
                                invoice_data['email_date'] = email_info.get('date_sent', 'Unknown')
                                invoice_data['mbox_path'] = mbox_path
                                
                                self.invoices_data.append(invoice_data)
                                found_match = True
                
                if not found_match:
                    print(f"Could not find matching .emlx file for email: {email_info.get('subject', 'Unknown')}")
                    
            except Exception as e:
                print(f"Error processing email {email_info.get('subject', 'Unknown')}: {str(e)}")
                continue
        
        # Create DataFrame
        df = pd.DataFrame(self.invoices_data)
        return df
    
    def fallback_search_emlx_files(self) -> pd.DataFrame:
        """Fallback method: search all .emlx files directly"""
        print("Performing direct search of .emlx files...")
        
        # Search all account directories
        for account_dir in os.listdir(self.mail_data_path):
            if account_dir == "MailData":
                continue
                
            account_path = os.path.join(self.mail_data_path, account_dir)
            if not os.path.isdir(account_path):
                continue
            
            print(f"Searching account directory: {account_dir}")
            
            # Search all mbox directories
            for mbox_name in os.listdir(account_path):
                if mbox_name.endswith('.mbox'):
                    mbox_path = os.path.join(account_path, mbox_name)
                    print(f"  Searching mbox: {mbox_name}")
                    
                    emlx_files = self.find_emlx_files_in_mbox(mbox_path)
                    print(f"    Found {len(emlx_files)} .emlx files")
                    
                    for emlx_path in emlx_files:
                        try:
                            if self.check_emlx_for_paul_bandarian_invoice(emlx_path):
                                print(f"    Found matching email: {emlx_path}")
                                
                                # Extract PDFs from email
                                pdf_attachments = self.extract_attachments_from_emlx(emlx_path)
                                
                                for pdf_data in pdf_attachments:
                                    # Extract text from PDF
                                    pdf_text = self.extract_text_from_pdf(pdf_data)
                                    
                                    # Parse invoice data
                                    invoice_data = self.parse_invoice_data(pdf_text)
                                    invoice_data['emlx_path'] = emlx_path
                                    invoice_data['mbox_path'] = mbox_path
                                    
                                    self.invoices_data.append(invoice_data)
                        except Exception as e:
                            # Skip files that can't be read
                            continue
        
        # Create DataFrame
        df = pd.DataFrame(self.invoices_data)
        return df
    
    def check_emlx_matches_criteria(self, emlx_path: str, email_info: Dict) -> bool:
        """Check if .emlx file matches our search criteria"""
        try:
            with open(emlx_path, 'rb') as f:
                # Skip the first line which contains the message length
                f.readline()
                email_content = f.read()
            
            # Convert to string for searching
            content_str = email_content.decode('utf-8', errors='ignore')
            
            # Check for Paul Bandarian and Invoice
            return ('paul.bandarian@gmail.com' in content_str.lower() and 
                    'invoice' in content_str.lower())
                    
        except Exception:
            return False
    
    def check_emlx_for_paul_bandarian_invoice(self, emlx_path: str) -> bool:
        """Check if .emlx file is from Paul Bandarian with Invoice in subject"""
        try:
            with open(emlx_path, 'rb') as f:
                # Skip the first line which contains the message length
                f.readline()
                email_content = f.read()
            
            # Convert to string for searching
            content_str = email_content.decode('utf-8', errors='ignore')
            
            # Check for Paul Bandarian and Invoice
            return ('paul.bandarian@gmail.com' in content_str.lower() and 
                    'invoice' in content_str.lower())
                    
        except Exception:
            return False

def main():
    """Main function to run the Apple Mail invoice extractor"""
    
    # Create extractor instance
    extractor = AppleMailInvoiceExtractor()
    
    try:
        # Process all invoices
        df = extractor.process_all_invoices()
        
        if df.empty:
            print("No invoice data found.")
            return None
        
        # Display results
        print("\nInvoice Data Extracted:")
        print("=" * 50)
        print(df.to_string(index=False))
        
        # Save to CSV
        output_file = f"paul_bandarian_invoices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\nData saved to: {output_file}")
        
        return df
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    # Run the extractor
    df = main()