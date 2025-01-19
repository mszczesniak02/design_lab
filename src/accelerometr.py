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
YMAX =  5500
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
        if received is not None:
            return received
    return b"" 

def is_utf8(data):
    try:
        # Sprawdzenie, czy dane można przekonwertować na UTF-8
        data.decode('utf-8')
        return True
    except UnicodeError:
        return False

def main():
    print("Startowanie...\n")
    uart = UART(UARTNUM, BAUDRATE )                         
    uart.init(tx=Pin(TXPIN), rx=Pin(RXPIN) )
    x_val_array = [0] * 100 
    index_x = 0
    y_val_array = [0] * 100 
    index_y = 0
    
    # set initial X engine
    XPWM.duty_u16(XSTOP)
    time.sleep(0.5)
    YPWM.duty_u16(YMID)
    curr = YMID
    
    print("Startowanie: OK")
    while True:
        direction = detect_command(uart).strip()
        
        if not direction:
            continue
        utf = is_utf8(direction)
        if utf == False:
            continue
        if len(bts(direction)) != 11:
            continue
        x_byte = direction[1:5]
        x_val = x_byte.decode('utf-8')
        
        y_byte = direction[7:11]
        y_val = y_byte.decode('utf-8')
        
        print(x_val)
        print(y_val)
        
        XPWM.duty_u16(int(x_val))
        YPWM.duty_u16(int(y_val))
        time.sleep(0.1)
            
main()
