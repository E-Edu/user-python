import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email():

    def sendmail(): #send mail with Token to user

        #TODO: add Token from Database to mail

        port = 465 # ssl port
        password = "password"   #password for login on mailserver
        host = "host"        #mailserver
        sender_mail = "wirvsvirus@host.com"  #address from which the mail is sent
        receiver_mail = "receiver@mail.com"  #mail receiver
        subject = "Token for verification"  #subject of mail
        body = open('./mail.html')      #main body of mail
        message = body.read()     


        msg = MIMEMultipart() #message of mail
        msg["From"] = sender_mail
        msg["To"] = receiver_mail
        msg["Subject"] = subject
        msg.attach(MIMEText(message, 'html'))
        print(msg)

        server = smtplib.SMTP_SSL(host, port)   # init server
        server.connect(host, port)      #connect to server
        server.login(sender_mail, password) #login at server
        print("connected!")

        server.sendmail(sender_mail, receiver_mail, msg.as_string())    #send the mail
        print("Mail sent!")
        server.close()      #disconnect from server



    def verifymail(token): #check token from email for verification

        #TODO: open database and get token of specific user, set accountStatus to 1 in database

        if token == dbtoken:    #check if entered token
            accountStatus = 1
        else:
            return 200