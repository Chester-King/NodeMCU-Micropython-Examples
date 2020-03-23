import time
import machine

buttonPin = machine.Pin(2,  machine.Pin.IN, machine.Pin.PULL_UP)
ledPin = machine.Pin(4, machine.Pin.OUT)

while(True):
    buttonState = buttonPin.value()
    if(buttonState == 1):
        ledPin.on()
    else:
        ledPin.off()
