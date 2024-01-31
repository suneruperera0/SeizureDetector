# while True:
#     if button.is_pressed:
#         print("Patient is not having a seizure")
#     else:
#         print("Patient is having a seizure")

#     # button.wait_for_press()
#     # print("Button was pressed")

def buttonFailSafe():
    while True:
        if button.is_pressed:
            print("Patient is not having a seizure. False alarm.")
        else:
            print("Patient is having a seizure. Call 911. ")