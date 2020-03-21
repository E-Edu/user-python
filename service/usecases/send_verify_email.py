import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_verify_email(email):  # send mail with Token to user

    # TODO: add Token from Database to mail

    port = 465 # ssl port
    password = os.environ["EMAIL_PASSWORD"]
    host = os.environ["EMAIL_HOST"]
    sender_mail = os.environ["EMAIL_EMAIL"]
    receiver_mail = email
    subject = "Verify Email"
    body = open('resources/verify_email_template.html')  # TODO check path
    message = body.read()

    msg = MIMEMultipart()  # message of mail
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg["Subject"] = subject
    msg.attach(MIMEText(message, 'html'))
    print(msg)

    server = smtplib.SMTP_SSL(host, port)
    server.connect(host, port)
    server.login(sender_mail, password)
    print("connected!")

    server.sendmail(sender_mail, receiver_mail, msg.as_string())
    print("Mail sent!")
    server.close()

