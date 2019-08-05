from time import sleep
import RPi.GPIO as GPIO

# assign LED pin number to a variable
lightPin = 4
# assign button pin number to a variable
buttonPin = 17

# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number,
# as you can see on breadboard printed schema
GPIO.setmode(GPIO.BCM)

# tell the system the an LED pin will be an output (we will send data there)
GPIO.setup(lightPin, GPIO.OUT)

# tell the system the an BUTTON pin will be an input (we will receive data from there)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# this while cycle infinitely checks the state of a button on the breadboard every 0.1 seconds (100 milliseconds)
# and send updated data to a breadboard
while True:
    # response values for button from a breadboard
    buttonIsPressed = 0
    buttonIsReleased = 1

    # request values for LED to a breadboard
    lightIsOn = 1
    lightIsOff = 0

    # read the current button state from breadboard
    currentButtonState = GPIO.input(buttonPin)

    # make a decision what to do based on the button state
    if currentButtonState == buttonIsPressed:
        # if the button is pressed set the state of the LED to true
        ledState = lightIsOn 
    elif currentButtonState == buttonIsReleased:
        # otherwise, if the button is not pressed, set the state of the LED to off
        ledState = lightIsOff
    
    # send the state of the LED to breadbord, so it can turn a light on or off
    GPIO.output(lightPin, lightState)

    # this prevents code from running to fast and using too much resources
    # we stop everything for 0.01 seconds as humans can't press the button faster than 10 times per second
    sleep(.10)