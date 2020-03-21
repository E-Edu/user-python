from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import database as db
import smtplib

dbs = db.Database

class ForgotPassword():

    def __init__(self, user_email):
        if dbs.getUserIdByEmail(user_email) is not None:
            self.isvalid = True
            self.sender_adress = "wirvsvirus@ampferl.com"
            self.sender_pw = "Kvvm83#4?92Hqqx3"
            self.host = "ampferl.com"
            self.port = 465
            self.message = open('./pwmail.html').read()
            self.subject = "Passwort reset for E-Edu"
            self.user_email = user_email
            self.msg = MIMEMultipart()  # message of mail
            self.msg["From"] = self.sender_adress
            self.msg["To"] = self.user_email
            self.msg["Subject"] = self.subject
            self.msg.attach(MIMEText(self.message, 'html'))
        else:
            self.isvalid = False

    def sendMail(self):
        if self.isvalid:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.connect(self.host, self.port)
            server.login(self.sender_adress, self.sender_pw)
            print("connected!")
            server.sendmail(self.sender_adress,[self.user_email],self.message)
            print("Sending complete")
            server.close()

ForgetPassword("nbsteini@gmail.com").sendMail()