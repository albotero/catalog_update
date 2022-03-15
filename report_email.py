#!/usr/bin/env python3

'''
From: automation@example.com
To: username@example.com
Replace username with the username given in the Connection Details Panel on the right hand side.
Subject line: Upload Completed - Online Fruit Store
E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
Attachment: Attach the path to the file processed.pdf
'''

from datetime import datetime
from emails import generate_email, send_email
from reports import generate_report

def main():
    hoy = datetime.now().strftime('%B %-d, %Y')
    tempfile = '/tmp/processed.pdf'
    generate_report(
        'supplier-data/descriptions',
        tempfile,
        'Processed update on {}'.format(hoy))

    email_from = 'automation@example.com'
    email_to = 'student-02-2fcef9f5ba3b@example.com'
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    msg = generate_email(email_from, email_to, email_subject, email_body, tempfile)
    send_email(msg)

main()
