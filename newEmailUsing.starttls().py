import smtplib, ssl
# from unittest.mock import sentinel

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "1P10DP3code@gmail.com"
receiver_email = "somethingemail@gmail.com" #make sure to put another email in here that it will be sent to
password = input("Type your password and press enter: ") 
message = """\
    Subject: Hi there

    This message is sent from Python."""

#Creating a secure SSL context
context = ssl.create_default_context()

#Trying to log into server and send email

# try:
#     server = smtplib.SMTP(smtp_server, port)
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() #can get rid of since it isn't necessarily needed
    server.starttls(context=context) #secures the connection
    server.ehlo() #can get rid of since it isn't necessarily needed
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    #type the email here??
# except Exception as e:
#     #print any error messages to stdout
#     print("An error has occured")
#     print(e)
# finally:
#     server.quit()
