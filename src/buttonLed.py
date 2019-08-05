from time import sleep
import RPi.GPIO as GPIO

# GPIO pins of components

# assign LED pin number to a variable
lightPin = 4
# assign button pin number to a variable
buttonPin = 17

# set up BCM GPIO numbering 
# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)


# set a LED pin as an output
GPIO.setup(lightPin, GPIO.OUT)

# set a button pin as an input
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    lightOn = 0 if GPIO.input(buttonPin) == 1 else 1
    GPIO.output(lightPin, lightOn)
    sleep(.01)