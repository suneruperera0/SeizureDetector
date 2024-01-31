import smtplib
import time
#https://docs.python.org/3/library/email.examples.html 

# From = "delbalsv@mcmaster.ca" #switch to mcmaster email after smpt server is created
# To = ["pererv3@mcmaster.ca"]

from email.message import EmailMessage

# import time 
# seconds = 0 
# minutes = 0
# hours = 0

# while True:
#   for seconds in range(-1,60):
#     seconds += 1
#     time.sleep(0.1)
#     print(seconds)
   
# while True:
#   for minutes in range (-1,60):
#     minutes += 1
#     time.sleep(6)
#     print(minutes)
    # print(minutes + "\t")

  # for hours in range (-1,24):
  #   hours += (1)
  #   time.sleep(3600)
    # print(hours + "\t")
#for some reasong the counter underlines the email code...
#fix formatting of timer and figure out how to make it not underline email 






#trying to write the .txt file
def write_file(textfile):
    message = "Patient is having a seizure. Call 911."
    newfile = open(str(textfile), "w")
    newfile.write(str("This person is having a seizure. Call 911."))
    newfile.close


    with open(textfile) as fp: #or should textfile be switched with newfile^
        msg = EmailMessage()
        msg.set_content(fp.read())

        me = "delbalsv@mcmaster.ca" # change to a .python email after setting up smpt server
        you = ["pererv3@mcmaster.ca"]
        
        msg['Subject'] = f'The contents of {textfile}' #understand what this means
        msg['From'] = me
        msg['To'] = you

        s = smtplib.SMPT('localhost')
        s.send_message(msg)
        s.quit

