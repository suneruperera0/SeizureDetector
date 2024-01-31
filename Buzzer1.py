from gpiozero import Buzzer
import time
import sys

def buzzer_alarm(buzzer_object):
    buzzer_object = Buzzer(27)

    if rollingAvg > basalRate:
        buzzer_object.on()
        time.sleep(1)
    else:
        buzzer_object.off()

    