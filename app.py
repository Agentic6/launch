import re
import csv

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_emails_from_text(text):
    # Assuming each email starts with "From " and ends with a blank line
    emails = text.split('\n\nFrom ')
    emails = ['From ' + email.strip() for email in emails if email.strip()]
    return emails

def parse_email_for_bounced_address(email_text):
    # Find lines that indicate a bounced email address
    bounced_address = None
    for line in email_text.split('\n'):
        if 'Final-Recipient' in line:
            bounced_address = line.split(';')[-1].strip()
            break
    return bounced_address

def extract_bounced_addresses(emails):
    bounced_addresses = []
    for email_text in emails:
        bounced_address = parse_email_for_bounced_address(email_text)
        if bounced_address:
            bounced_addresses.append(bounced_address)
    return bounced_addresses

def save_to_csv(email_addresses, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Bounced Email Addresses"])
        for email in email_addresses:
            writer.writerow([email])

def main():
    file_path = 'path/to/your/text/file.txt'  # Replace with the path to your text file
    text = read_text_file(file_path)
    emails = parse_emails_from_text(text)
    bounced_addresses = extract_bounced_addresses(emails)
    save_to_csv(bounced_addresses, 'bounced_emails.csv')

if __name__ == "__main__":
    main()
