#use gmail smtplib server to send emails

import smtplib, ssl #imports the ssl initiates a TLS-encrypted connection

port = 465
password = input("Type your password and press enter: ")

#creating a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login("1P10DP3code@gmail.com", password)

    #This email has come through