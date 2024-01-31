import time

counter = 0
while counter < 20:
    print("Press the button if you would like to temporarily stop the program.")
    counter+=1
    time.sleep(1)
    print(counter)
