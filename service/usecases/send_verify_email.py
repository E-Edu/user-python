import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_verify_email(email):

    # TODO: add Token from Database to mail

    port = os.environ["SMTP_PORT"] # ssl port
    password = os.environ["SMTP_PASSWORD"]
    host = os.environ["SMTP_HOST"]
    sender_mail = os.environ["SMTP_USERNAME"]
    receiver_mail = email
    subject = "Verify Email"
    body = open('resources/verify_email_template.html')  # TODO check path
    message = body.read()

    msg = MIMEMultipart()  # message of mail
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg["Subject"] = subject
    msg.attach(MIMEText(message, 'html'))

    server = smtplib.SMTP_SSL(host, port)
    server.connect(host, port)
    server.login(sender_mail, password)

    server.sendmail(sender_mail, receiver_mail, msg.as_string())
    server.close()
