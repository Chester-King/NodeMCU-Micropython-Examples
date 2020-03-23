import machine
import time

buttonPin = machine.Pin(2,  machine.Pin.IN, machine.Pin.PULL_UP)
ledPin = machine.Pin(4, machine.Pin.OUT)

buttonPushCounter = 0
buttonState = 0
lastButtonState = 0

while(True):
    buttonState = buttonPin.value()

    if(buttonState != lastButtonState):
        if(buttonState == 1):
            buttonPushCounter += 1
            print("on")
            print("number of button pushes: ", buttonPushCounter)
        else:
            print("off")
        time.sleep_ms(50)
    lastButtonState = buttonState

    if(buttonPushCounter % 4 == 0):
        ledPin.value(1)
    else:
        ledPin.value(0)
