import time
import machine

pin = machine.Pin(14, machine.Pin.OUT)

pin1 = machine.Pin(2, machine.Pin.OUT)
pin2 = machine.Pin(16, machine.Pin.OUT)

while(True):
    pin1.on()
    time.sleep(1)
    pin1.off()
    time.sleep(2)
