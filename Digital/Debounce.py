import machine
import time

buttonPin = machine.Pin(2,  machine.Pin.IN, machine.Pin.PULL_UP)
ledPin = machine.Pin(4, machine.Pin.OUT)

ledState = 1
buttonState = 0
lastButtonState = 0

lastDebounceTime = 0
debounceDelay = 0

ledPin.value(ledState)

while(True):
    reading = buttonPin.value()

    if(reading != lastButtonState):
        lastDebounceTime = int(round(time.time() * 1000))
    if((int(round(time.time() * 1000))-lastDebounceTime) > debounceDelay):
        if(reading != buttonState):
            buttonState = reading
            if(buttonState == 1):
                ledState = 0 if ledState == 1 else 1
    ledPin.value(ledState)
