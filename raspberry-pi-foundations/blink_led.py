#Simple blink led sketch using GIPO pin on RaspberryPi

from gipozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)