#! /usr/bin/python

"""
Func adapted from https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
Formatting of email adapted from https://realpython.com/python-send-email/
"""

# Imports
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from imap_tools import MailBox, AND
import os
from dotenv import load_dotenv


def send_email(subject, body, filepath):
    load_dotenv()

    print("[INFO] sending email.")

    # Create a multipart message and set headers

    recipient = os.getenv("RECIPIENT")
    FROM = os.getenv("USER_EMAIL")
    pwd = os.getenv("USER_PASSWORD")

    email = MIMEMultipart()
    email["From"] = FROM
    email["To"] = recipient
    email["Subject"] = subject
    # email["Bcc"] = recipient

    # Add body to email
    email.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filepath}",
    )

    # Add attachment to message and convert message to string
    email.attach(part)
    text = email.as_string()

    # Send actual email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, pwd)
        server.sendmail(FROM, recipient, text)
        server.close()
        print("[INFO] successfully sent email.")

    except:
        print("[ERROR] failed to send email.")


def receive_email():
    load_dotenv()

    mb = MailBox('imap.gmail.com').login(os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD"))

    # Fetch all unseen emails containing "electricity.com" in the from field
    # Don't mark them as seen
    # Set bulk=True to read them all into memory in one fetch
    # (as opposed to in streaming which is slower but uses less memory)
    messages = mb.fetch(criteria=AND(seen=False, from_=os.getenv("RECIPIENT")),
                        mark_seen=True,
                        bulk=False)
    for msg in messages:
        return msg.text
