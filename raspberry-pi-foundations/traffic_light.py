from gpiozero import LED
from time import sleep

# LED PIN ASSIGNMENTS
red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
    # RED
    red.on()
    sleep(5)
    red.off()

    # GREEN
    green.on()
    sleep(5)
    green.off()

    # YELLOW
    yellow.on()
    sleep(2)
    yellow.off()