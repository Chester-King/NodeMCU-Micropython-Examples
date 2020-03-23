import time
import math
import machine

pd4 = machine.Pin(2)
led = machine.PWM(pd4, freq=1000)
fadeAmount = 0.5
brightness = 0

while(True):
    led.duty(int(math.sin(brightness / 10 * math.pi) * 500 + 500))
    brightness = brightness + fadeAmount
    if(brightness <= 0 or brightness >= 255):
        fadeAmount = -fadeAmount
    time.sleep_ms(30)
