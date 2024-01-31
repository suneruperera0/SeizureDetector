import smtplib, ssl
def sendEmail():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "1P10DP3code@gmail.com"
    receiver_email = "1p10dp3codesent@gmail.com" 
    password = input("Type your password and press enter: ") 
    message = """\
        Subject: Hi there

        This message is sent from Python."""

    #Creating a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
sendEmail()