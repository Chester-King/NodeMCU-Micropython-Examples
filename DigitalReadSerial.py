import time
import machine

pushButton = machine.Pin(2,  machine.Pin.IN, machine.Pin.PULL_UP)

while(True):
    buttonState = pushButton.value()
    print(buttonState)
    time.sleep_ms(1)
