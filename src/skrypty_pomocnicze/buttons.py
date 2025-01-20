from machine import UART, Pin
from machine import PWM
import time

###         UART SETUP
TXPIN = 16
RXPIN = 17
UARTNUM = 0
BAUDRATE = 9600

###         PWM SETUP
XPWM = PWM(Pin(15)) 
YPWM = PWM(Pin(3)) 
XPWM.freq(50)
YPWM.freq(50)

###         ENGINES MIN MAX
YMAX =  5800
YMID =  5000
YMIN =  4900 
YCURRENT = YMID

XRIGHT  = 5200
XSTOP   = 4800
XLEFT   = 4510

        
###       DATA CONVERSION
def bts(dane):
    if isinstance(dane, bytes):
        return dane.decode('utf-8')  
    else:
        raise ValueError("Błąd konwersji")

def detect_command(uart):
    direction = ""
    if uart.any():
        received = uart.read()  
        direction = bts(received) 
        print(f"Wykryto:{direction}")
    return direction

def main():
    print("Startowanie...\n")
    uart = UART(UARTNUM, BAUDRATE )                         
    uart.init(tx=Pin(TXPIN), rx=Pin(RXPIN) )

    # set initial X engine
    XPWM.duty_u16(XSTOP)
    time.sleep(0.5)
    YPWM.duty_u16(YMID)
    curr = YMID
    
    print("Startowanie: OK")
    while True:
        direction = detect_command(uart).strip()
 
        if direction == 'R':
            XPWM.duty_u16(XRIGHT)
            time.sleep(0.5)
            

        elif direction  == "L":
            XPWM.duty_u16(XLEFT)
            time.sleep(0.5)
        
        elif direction  == "G":
            curr += 50
            print(curr)
            if curr <= YMAX and curr >= YMIN:
                YPWM.duty_u16(curr)
                time.sleep(0.5)
            else:
                curr = YMAX
                YPWM.duty_u16(curr)
                time.sleep(0.5)
        elif direction  == "D":
            curr -= 50
            print(curr)
        
            if curr <= YMAX and curr >= YMIN:
                YPWM.duty_u16(curr)
                time.sleep(0.5)
            else:
                curr = YMIN
                YPWM.duty_u16(curr)
                time.sleep(0.5)
        else:
            XPWM.duty_u16(XSTOP)
            
           

main()
