import machine
import time

sensorVal = machine.Pin(2,  machine.Pin.IN, machine.Pin.PULL_UP)
outputPin = machine.Pin(4, machine.Pin.OUT)

while(True):
    print(sensorVal.value())
    if(sensorVal.value() == 1):
        outputPin.value(0)
    else:
        outputPin.value(1)
