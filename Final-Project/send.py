import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_directory = os.getcwd() + "/Final-Project/receiver_list.txt"


def attachment(server, email, subject, text):
    try:
        with open(email_directory) as file:
            receiver_emails = file.read().split(",")
            for receiver_email in receiver_emails:
                message = MIMEMultipart()
                message["subject"] = subject
                message["From"] = email
                message["To"] = receiver_email

                # Add body to email
                message.attach(MIMEText(text, "plain"))

                with open(email_directory, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                    encoders.encode_base64(part)

                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= receiver_list.txt"
                    )

                    message.attach(part)
                    text = message.as_string()

                server.sendmail(email, receiver_email,text )
                print("Email sent to ", receiver_email) 
    except:
        return print("failed to send message")

def message(server, email, subject, text):
    try:
        message = 'Subject: {}\n\n{}'.format(subject, text)

        with open(email_directory) as file:
            receiver_emails = file.read().split(",")

            for receiver_email in receiver_emails:
                server.sendmail(email, receiver_email, message)
                print("Email sent to ", receiver_email)    
    except:
        return print("failed to send message")