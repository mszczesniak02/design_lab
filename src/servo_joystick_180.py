import time
from machine import Pin, PWM, ADC

x = ADC(Pin(27))

pwm = PWM(Pin(0))
pwm.freq(50)

while True:
        xval = x.read_u16()
        duty = round(xval/7.71)
        if xval < 15600:
            duty = 2000
        elif (xval > 33000 and xval < 35000):
            duty = 5200
        pwm.duty_u16(duty)
        print("X: " + str(xval) + " duty: " + str(duty))
