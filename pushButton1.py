import time 
import GPIO

def pushButton ():
    userButton = button(13)
    counter = 1
    timer = 0
#make timer#

    
    while timer < 20: #switch while True to sensor data greater than basal
        #put yellow warning light pin on
        if userButton.is_pressed == True:
            counter += 1
            if counter % 2 == 0:
                print("You are not having a seizure")

            elif counter % 2 == 1:
                #put red LEDs on **use the multuple LED demo example (final example in lab)
                #buzzer goes on
                print ("You are having a seizure")
                #send email
                

