#Names, MacID: Victoria Del Balso, 400384960
#              Seniru Perera, 400391618
#Team Number:  Team 19

from sensor_library import Muscle_Sensor
from gpiozero import Buzzer
from gpiozero import LED
from gpiozero import Button
import sys
import time
import smtplib, ssl
import time 

# crfpeedkdtvhawla
# ^email password

#buzzer_object = Buzzer(27)
#buzzer_object.off()
#led1 = LED(5)
#led2 = LED(19)
#led3= LED(26)
#led1.off()
#led2.off()
#led3.off()

#function to have constant data input 
def inputData(dataList0, dataList1, sensor0Raw, sensor1Raw, sensor0, sensor1):
    sensor0Raw = sensor0.muscle_raw() 
    sensor1Raw = sensor1.muscle_raw()
    if len(dataList0) > 10 and len(dataList1) > 10: 
        del dataList0[0] #deletes the first appendix of each list if the list length > 10
        del dataList1[0]   
    dataList0.append(sensor0Raw) #appends a value and replaces the first index of the list
    dataList1.append(sensor1Raw)
    return sensor0Raw, sensor1Raw #returns values to print the most recent value when called in main()

#function calculating the rolling average of 10 data points from two sensors each 
def calculateRollingAvg(dataList0, dataList1):
    rollingAvg = (sum(dataList0) + sum(dataList1)) / (len(dataList0) + len(dataList1))
    return rollingAvg #returns rollingAvg to print the most recent value when called in main()

#function writing a header to an empty document
def columnHeader():
    newFile = open('medDoc.txt', "w") 
    newFile.write("The patient's EMG Average is: ") #only one column header required for medical document
    newFile.close()

#function appending the data to the medical document
def appendFile(rollingAvg): #only rollingAvg is required for medical document 
    with open('medDoc.txt', 'a+') as fileObject: #syntax means that newFile.close() does not need to be explicitly written
        fileObject.seek(0) #read cursor is looking for the first line of text so that a new line can be written after
        data = fileObject.read(1000) #reads 1000 bytes of data
        if data != None: #appending to the file if there is text (i.e. column header already written in document)
            fileObject.write("\n") 
            fileObject.write(str(rollingAvg)) #converts to string so that it can be written to file

#function that sends an email if seizure is occuring
##def sendEmail(rollingAvg,basalRate):
def sendEmail(): #no arguments because email only sends if conditional statement is met
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "1P10DP3code@gmail.com"
    receiver_email = "1P10DP3codesent@gmail.com"
    password = input("Type your password and press enter: ") #required each time as a security measure (proof of concept)
    emailTxtSeizure = """\
        Subject: Seizure

        This patient is having a seizure. """
    # """\ is a syntax to have it format correctly
    context = ssl.create_default_context() #required to send email 
    with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, emailTxtSeizure)         

#function which alerts people using buzzer and LEDs
#function is stopped for 20 minutes (time.sleep(1200)) if button is pressed. This signifies a seizure is not happening
def alarm(rollingAvg, basalRate, push_button, buzzer_object, led1, led2, led3, have_seizure):
    for counter in range(10, 0, -1): 
        if have_seizure: #have_Seizure is initialized in main() as a boolean
            print("Press the button if you would like to temporarily stop the program")
            print(counter)
        time.sleep(1)
        if push_button.is_pressed:
            print("Patient is not having a seizure. False alarm")
            print("Buzzer is off","\n","LEDs are off","\n")
            time.sleep(30) #proof of concept. Would normally be time.sleep(1200) but for sake of presentation --> 30 seconds 
            have_seizure=False
            buzzer_object.off()
            led1.off()
            led2.off()
            led3.off()
            return have_seizure      
    if have_seizure: #have_seizure is True in main()
        
        print("Patient is having a seizure. Call 911")
        buzzer_object.on()
        led1.on()
        led2.on()
        led3.on()
        print("Buzzer is on","\n","LEDs are on","n")

#function for print statements of the rollingAvg, rad data from sensor 1, raw data from sensor 2
#printing the states of outputs is not called in this function to have simpler code. Instead, it is printed in alarm()
def printStatements(rollingAvg, rawDataList):
    print("The rolling average is", rollingAvg)
    print("The raw muscle data from sensor 1 is", rawDataList[0])
    print("The raw muscle data from sensor 2 is", rawDataList[1], "\n")
    
#defining a function to kill the program for proof of concept.
#in real life, outputs would continue
#for the sake of the presentation, killFunction will be called in shell to turn off output devices
def killFunction(buzzer_object, led1, led2, led3):
    buzzer_object.off()
    led1.off()
    led2.off()
    led3.off()

#main() function calls functions (i.e. calculateRollingAvg(), alarm(), etc.)    
def main():

    #defining variables and objects
    buzzer_object = Buzzer(27)
    push_button = Button(13)
    led1 = LED(5)
    led2 = LED(19)
    led3 = LED(26)
    sensor0 = Muscle_Sensor(0)
    sensor1 = Muscle_Sensor(1)
    sensor0Raw = sensor0.muscle_raw()
    sensor1Raw = sensor1.muscle_raw()
    dataList0 = []
    dataList1 = []
    basalRate = 90 

    #calling function to write column headers
    #called outside of while True loop to prevent columnHeader() from deleting data and writing a new file after each iteration
    #no arguments passing through since writing happens due to the dot operator .write()
    columnHeader()

    #intializing a boolean variable to True
    #boolean is changed depending on if a seizure is happening (dependent on if button is pressed)
    #boolean is returned in the alarm() function
    have_seizure = True

    #ensures that the newer data is printed instead of old data
    
    rawDataList = []
    while True:
        #calling function with constant data input from two sensors
        rawDataList = inputData(dataList0, dataList1, sensor0Raw, sensor1Raw, sensor0, sensor1)
        #calling function which calculates the rolling average of two sensors
        rollingAvg = calculateRollingAvg(dataList0, dataList1)
        #calling function which appends data to a file 
        appendFile(rollingAvg)
        #calling function which prints the rollingAvg
        printStatements(rollingAvg, rawDataList)

        #conditional statement for abnormal muscle activity
        if rollingAvg > basalRate:
            have_seizure = alarm(rollingAvg, basalRate, push_button, buzzer_object, led1, led2, led3, have_seizure)
            have_seizure = sendEmail()
            printStatements(rollingAvg, rawDataList) #called again so this prints no matter if a seizure occurs
            
main()










