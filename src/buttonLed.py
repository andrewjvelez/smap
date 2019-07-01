from time import sleep
import RPi.GPIO as GPIO

# GPIO pins of components
lightPin = 4
buttonPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    lightOn = 0 if GPIO.input(buttonPin) == 1 else 1
    GPIO.output(lightPin, lightOn)
    sleep(.01)