import machine
import time

pd4 = machine.Pin(2)  # Servo connected on D4
servo = machine.PWM(pd4, freq=50)
while(1):
    for x in range(40, 115):
        servo.duty(x)
        time.sleep_ms(15)
    for x in range(115, 40, -1):
        servo.duty(x)
        time.sleep_ms(15)
