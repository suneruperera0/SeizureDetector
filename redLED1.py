import sys
from gpiozero import LED
import time
import sys

def seizureRedLED():
    redLED1 = LED()
    redLED2 = LED()
    redLED3 = LED()

    while True:
        if button.is_pressed:
            redLED1.off()
            redLED2.off
            redLED3.off
        elif button.is_not_pressed:
            redLED1.on ()
            redLED2.on ()
            redLED3.on ()
