from sensor_library import Muscle_Sensor
from datetime import datetime 
import time 
from gpiozero import Buzzer
from gpiozero import LED
import sys



#calculating the rolling average
def calcAvg(dataList0, dataList1):
    rollingAvg = (sum(dataList0) + sum(dataList1)) / (len(dataList0) + len(dataList1))
    return rollingAvg



#writing column headers in the new .txt file
def columnHeaders(medDoc):
    newFile = open(medDoc, "w")
    newFile.write("Rolling Average") #fix column headers 
    newFile.close()



#appending rolling average to the file
def appendFile (medDoc, rollingAvg, timer, clock):
    newFile = open(medDoc, "a") #a not w because w gets rid of everything in the file whereas a adds to the file
    for item in rollingAvg: #and time stamp
        newFile.write(item[0] + "\t" + item[1] + "\n" )
    newFile.close()
#**finish this one**

# append_array(fileName, nx2array):
#     newfile = open(str(fileName), "w")
#     for item in nx2array:
#         newfile.write(str(item[0]) + "\t" + str(item[1]) + "\n")
#     newfile.close()



#buzzer sounds if patient is having a seizure (button is not turned off)
#use the information from buttonFailSafe
#if button is not pressed, alarm goes off 
#should wait 20 seconds for button to be pressed
def buzzer_alarm(buzzer_object, rollingAvg, basalRate):
    buzzer_object = Buzzer(27)

    # if rollingAvg > basalRate:
    if button.is_not_pressed:
        buzzer_object.on()
        time.sleep(5)
    elif button.is_pressed:
        buzzer_object.off()
    else:
        buzzer_object.off


#button fail safe mechanism allowing the user to press the button to temporarily stop the program for 20 seconds
def buttonFailSafe(rollingAvg, basalRate):
    
    if rollingAvg > basalRate: 
        counter = 0
        while counter < 20:
            print("Press the button if you would like to temporarily stop the program.")
            #message prints multiple times to ensure that the patient is seeing it. 
            #less chance of a false positive
            counter+=1
            time.sleep(1)

        button.wait_for_press(counter) 
        if button.is_pressed:
            print("Patient is not having a seizure. False alarm.")
        else:
            print("Patient is having a seizure. Call 911.")




def warningYellowLED(rollingAvg, basalRate):
    yellowLED = LED(6)

    if rollingAvg > basalRate:
        # yellowLED.on(time.sleep(20))
        yellowLED.on()
        time.sleep(20)
    else:
        yellowLED.off()



#red lights turn on if the button is not pressed
def seizureRedLED(rollingAvg): 
    redLED1 = LED(5)
    redLED2 = LED(19)
    redLED3 = LED(26)

    if rollingAvg > 94:
        if button.is_pressed:
            redLED1.off()
            redLED2.off()
            redLED3.off()
        else:
            redLED1.on ()
            redLED2.on ()
            redLED3.on ()


import smtplib, ssl
def sendEmail():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "1P10DP3code@gmail.com"
    receiver_email = "1p10dp3codesent@gmail.com" 
    password = input("Type your password and press enter: ") 
    timeStamp = datetime.now()
    timeString = timeStamp.strftime("%d/%m/%Y %H:%M:%S")
    emailTxt = """\
        Subject: Seizure

        This person is having a seizure. This happened at """ + timeString

    #Creating a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, emailTxt)
sendEmail()





def main(): 

    sensor0 = Muscle_Sensor(0) 
    sensor1 = Muscle_Sensor(1) 
    basalRate = 94 #Aiden's basal rate #max is 243
    #make sure basal_rate isn't hardcoding 

    dataList0 = []
    dataList1 = []

    scale = 10  

    while True:
        try:
            #scaled output methods
            sensor0Scale = sensor0.muscle_scaled(scale) 
            sensor1Scale = sensor1.muscle_scaled(scale)
            
            #appending the data to a list
            dataList0.append(sensor0Scale)
            dataList1.append(sensor1Scale)

            #calculating rolling average call function 
            rollingAvg = calcAvg(dataList0, dataList1)





        

        
            #gives the raw output
            # sensor0Raw = sensor0.muscle_raw()
            # sensor1Raw = sensor1.muscle_raw()

            #appending the data to a list
            dataList0.append(sensor0Scale)
            dataList1.append(sensor1Scale)
            #if we want this in the .txt file, might need to be converted to str
        #should scale go into the lists? In the demonstration, raw value was used since resting activity was 94

    ###IMPORTANT###
    #Input sensor data, append to list, calc rolling average, output to a file, use rolling average in 2 defined functions



            # print (sensor0Scale)
            # print (sensor1Scale)

            # print (sensor0Raw)
            # print (sensor1Raw)
        except KeyboardInterrupt:
            ##turn off all LEDS, buzzer, and sent email
            sys.exit(0)







        
