# Dokumentacja Labyrinth

## Spis Treści
1. [Cel Projektu](#cel-projektu)
2. [Wykorzystane komponenty](#wykorzystane-komponenty)
   - [Raspberry Pi Pico](#raspberry-pi-pico)
   - [HC-06](#hc-06)
   - [SG90](#sg90)
   - [SG90-HV](#sg90-hv)
3. [Schematy połączeń](#schematy-polaczen)
   


## Cel Projektu
Celem projektu jest stworzenie gry w stylu mini-golfa, polegającej na umieszczeniu kuli w centralnym miejscu planszy poprzez odpowiednie omijanie przeszkód.

## Wykorzystane komponenty
Spis oraz opis komponentów niezbędnych do realizacji projektu gry "Labyrinth".

### Raspberry Pi Pico
W projekcie użyto mikrokontrolera Raspberry Pi Pico:
Odbiera dane z aplikacji i steruje pochyleniem planszy za pomocą dwóch serwomechanizmów. UART0 służy do odbierania danych z modułu HC-06, a sygnały PWM sterują serwami SG90 i SG90-HV odpowiednio do ruchów pionowych i poziomych.

### HC-06
Moduł Bluetooth umożliwia komunikację pomiędzy układami master i slave. Zasilany jest zewnętrznym źródłem 5V i podłączony w następujący sposób:
- **Rx**: GP17
- **Tx**: GP16
- **GND**: GND
- **Vcc**: Zewnętrzne źródło 5V

### SG90
Serwomechanizm użyty do pochylania planszy w pionie. Zasilany jest zewnętrznym źródłem 5V i podłączony w następujący sposób:
- **Pin sterujący**: GP3
- **Vcc**: Zewnętrzne źródło 5V
- **GND**: GND

### SG90-HV
Serwomechanizm użyty do pochylania planszy w poziomie. Zasilany jest zewnętrznym źródłem 5V i podłączony w następujący sposób:
- **Pin sterujący**: GP15
- **Vcc**: Zewnętrzne źródło 5V
- **GND**: GND

### Schemat połączeń układu 
**Moduł Bluetooth HC-06:**
- Rx → GP17
- Tx → GP16
- GND → GND
- Vcc → Zewnętrzne źródło 5V


**Serwomechanizm SG90:**
- GND → GND
- Vcc → Zewnętrzne źródło 5V
- Pin sterujący → GP3

**Serwomechanizm SG90-HV:**
- GND → GND
- Vcc → Zewnętrzne źródło 5V
- Pin sterujący → GP15
