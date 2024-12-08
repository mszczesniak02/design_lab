import time
from machine import Pin, PWM

pwm = PWM(Pin(0))
pwm.freq(50)

while True:
        pwm.duty_u16(5150) 
        #time.sleep(2)
        #pwm.duty_u16(2000) 
        #time.sleep(2)
        
#1000 szybko w prawo
#~3500 zwalnia
#4600 stop
#5200 wolno w lewo
#6600 szybko w lewo
#8700 stop