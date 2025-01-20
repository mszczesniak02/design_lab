import time
from machine import Pin, PWM

pwm = PWM(Pin(0))
pwm.freq(50)

while True:
    pwm.duty_u16(8500) #0 [8500] stopni 0.26% dla 50Hz 5.2 ms
    time.sleep(2)
    pwm.duty_u16(2000) #180 [2000] stopni 0.61% dla 50Hz 12.2 ms
    time.sleep(2)