import machine
import time

ledPin = machine.Pin(2, machine.Pin.OUT)
ledState = 0

previousMillis = 0
interval = 1000

while(True):
    currentMillies = int(round(time.time() * 1000))
    if((currentMillies-previousMillis) >= interval):
        previousMillis = currentMillies
        if(ledState == 0):
            ledState = 1
        else:
            ledState = 0
        ledPin.value(ledState)
