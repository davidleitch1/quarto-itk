#!/usr/bin/env python3

import os
import glob
from typing import List, Dict

class SimpleBandarianFinder:
    def __init__(self):
        """Simple email finder using emlx library"""
        self.mail_path = os.path.expanduser("~/Library/Mail")
        self.found_emails = []
        
        # Check if emlx library is available
        try:
            import emlx
            self.emlx = emlx
            print("✅ Found emlx library")
        except ImportError:
            print("❌ emlx library not found. Install with: pip install emlx")
            self.emlx = None
    
    def find_all_emlx_files(self) -> List[str]:
        """Find all .emlx files in the Mail directory"""
        print(f"🔍 Searching for .emlx files in: {self.mail_path}")
        
        # Use glob to find all .emlx files recursively
        pattern = os.path.join(self.mail_path, "**", "*.emlx")
        emlx_files = glob.glob(pattern, recursive=True)
        
        print(f"📧 Found {len(emlx_files)} total .emlx files")
        return emlx_files
    
    def find_bandarian_emails(self) -> List[Dict]:
        """Find all emails from paul.bandarian@gmail.com with 'invoice' in subject"""
        if not self.emlx:
            print("❌ Cannot proceed without emlx library")
            return []
        
        all_emlx_files = self.find_all_emlx_files()
        
        if not all_emlx_files:
            print("❌ No .emlx files found")
            return []
        
        print(f"🔍 Checking {len(all_emlx_files)} emails for Paul Bandarian invoices...")
        
        bandarian_invoices = []
        processed = 0
        errors = 0
        
        for filepath in all_emlx_files:
            processed += 1
            
            # Progress indicator every 100 files
            if processed % 100 == 0:
                print(f"  📊 Processed {processed}/{len(all_emlx_files)} files...")
            
            try:
                # Parse the emlx file
                message = self.emlx.read(filepath)
                
                # Check if it's from Paul Bandarian
                from_header = message.headers.get('From', '').lower()
                if 'paul.bandarian@gmail.com' not in from_header:
                    continue
                
                # Check if subject contains 'invoice'
                subject = message.headers.get('Subject', '').lower()
                if 'invoice' not in subject:
                    continue
                
                # This is a Paul Bandarian invoice email!
                email_data = {
                    'filepath': filepath,
                    'from': message.headers.get('From', ''),
                    'subject': message.headers.get('Subject', ''),
                    'date': message.headers.get('Date', ''),
                    'message_id': message.headers.get('Message-ID', ''),
                    'has_attachments': message.flags.get('attachment_count', 0) > 0 if hasattr(message, 'flags') else False
                }
                
                bandarian_invoices.append(email_data)
                print(f"  ✅ Found invoice: {email_data['subject']}")
                
            except Exception as e:
                errors += 1
                if errors <= 5:  # Only show first 5 errors
                    print(f"  ⚠️  Error reading {os.path.basename(filepath)}: {str(e)}")
                elif errors == 6:
                    print(f"  ⚠️  ... suppressing further error messages (total errors: {errors})")
                continue
        
        print(f"\n🎯 RESULTS:")
        print(f"  📧 Processed: {processed} email files")
        print(f"  ❌ Errors: {errors} files")
        print(f"  ✅ Found: {len(bandarian_invoices)} Paul Bandarian invoice emails")
        
        return bandarian_invoices
    
    def display_results(self, emails: List[Dict]):
        """Display the found emails in a nice format"""
        if not emails:
            print("\n❌ No emails found")
            return
        
        print(f"\n📄 FOUND {len(emails)} PAUL BANDARIAN INVOICE EMAILS:")
        print("=" * 80)
        
        for i, email in enumerate(emails, 1):
            print(f"\n📧 Email {i}:")
            print(f"  📁 File: {os.path.basename(email['filepath'])}")
            print(f"  📝 Subject: {email['subject']}")
            print(f"  👤 From: {email['from']}")
            print(f"  📅 Date: {email['date']}")
            print(f"  📎 Has Attachments: {'Yes' if email['has_attachments'] else 'No'}")
            print(f"  🔗 Full Path: {email['filepath']}")

def main():
    """Main function"""
    print("🔍 Simple Paul Bandarian Invoice Email Finder")
    print("=" * 60)
    print("🎯 Goal: Find all emails from paul.bandarian@gmail.com with 'invoice' in subject")
    print("=" * 60)
    
    finder = SimpleBandarianFinder()
    
    # Check if Mail directory exists
    if not os.path.exists(finder.mail_path):
        print(f"❌ Mail directory not found: {finder.mail_path}")
        return
    
    print(f"✅ Mail directory found: {finder.mail_path}")
    
    # Find the emails
    emails = finder.find_bandarian_emails()
    
    # Display results
    finder.display_results(emails)
    
    if emails:
        print(f"\n💾 SUCCESS: Found {len(emails)} invoice emails!")
        print("🔧 Next step: Add PDF processing to extract invoice data")
    else:
        print(f"\n🔧 TROUBLESHOOTING:")
        print("1. Make sure Paul Bandarian emails exist in Apple Mail")
        print("2. Check that emails have 'invoice' in the subject line")
        print("3. Verify the emlx library is working: pip install emlx")
        print("4. Try running with 'Full Disk Access' permission if needed")

if __name__ == "__main__":
    main()