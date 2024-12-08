from machine import UART, Pin

uart = UART(0, 9600)                         # init with given
uart.init(tx=Pin(16), rx=Pin(17))

while True:

    uart.write("SENDING...")
    
    if uart.any():
        received = uart.read()  # Decode received bytes to string
        print(f"Received: {received}")
    
    
