import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class Email:
    def sendmail(self, email):  # send mail with Token to user

        # TODO: add Token from Database to mail

        port = 465 # ssl port
        password = os.environ["EMAIL_PASSWORD"]
        host = os.environ["EMAIL_HOST"]
        sender_mail = os.environ["EMAIL_EMAIL"]
        receiver_mail = email
        subject = "Verify Email"
        body = open('mail.html')
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


    def verifymail(self, token): # check token from email for verification
        # TODO: open database and get token of specific user, set accountStatus to 1 in database
        dbtoken = None
        if token == dbtoken:
            accountStatus = 1
        else:
            return 200