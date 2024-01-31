from gpiozero import LED
import time
import sys

def warningYellowLED():
    yellowLED = LED()

    if rollingAvg > basalRate:
        yellowLED.on(time.sleep(20))
    else:
        yellowLED.off()
