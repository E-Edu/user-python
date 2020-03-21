import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email():

    def sendmail(): #send mail with Token to user

        port = 465 # ssl port
        password = "Kvvm83#4?92Hqqx3"   #password for login on mailserver
        host = "ampferl.com"        #mailserver
        sender_mail = "wirvsvirus@ampferl.com"  #address from which the mail is sent
        receiver_mail = "lasse-knauff@t-online.de"  #mail receiver
        subject = "Token for verification"  #subject of mail
        body = open('./mail.html')
        message = body.read()     #main body of mail


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
        #TODO: get dbtoken
        dbtoken = "1234"
        if token == dbtoken:    #check if entered token
            accountStatus = 1
        else:
            return 200

email.sendmail()