# Dokumentacja Labyrinth

## Spis Treści
1. [Cel Projektu](#cel-projektu)
2. [Wykorzystane komponenty](#wykorzystane-komponenty)
   - [Raspberry Pi Pico](#raspberry-pi-pico)
   - [Iduino ST1079](#iduino-st1079)
   - [HC-06](#hc-06)
   - [SG90](#sg90)
   - [SG90-HV](#sg90-hv)
   - [Plansza](#plansza)
3. [Schematy połączeń](#schematy-polaczen)
   - [Schemat połączeń układu master](#schemat-polaczen-ukladu-master)
   - [Schemat połączeń układu slave](#schemat-polaczen-ukladu-slave)
4. [Software](#software)

---

## Cel Projektu
Celem projektu jest stworzenie gry w stylu mini-golfa, polegającej na umieszczeniu kuli w centralnym miejscu planszy poprzez odpowiednie omijanie przeszkód.

---

## Wykorzystane komponenty
Spis oraz opis komponentów niezbędnych do realizacji projektu gry "Labyrinth".

### Raspberry Pi Pico
W projekcie użyto dwóch mikrokontrolerów Raspberry Pi Pico:
- **Master**: Odpowiada za sterowanie układem slave przy użyciu joysticka Iduino ST1079 oraz modułu Bluetooth HC-06. Master wykorzystuje ADC0 i ADC1 do odczytu wartości z joysticka i wysyła przetworzone dane przez UART0 do układu slave za pomocą Bluetooth.
- **Slave**: Odbiera dane z układu master i steruje pochyleniem planszy za pomocą dwóch serwomechanizmów. UART0 służy do odbierania danych z modułu HC-06, a sygnały PWM sterują serwami SG90 i SG90-HV odpowiednio do ruchów pionowych i poziomych.

### Iduino ST1079
Analogowy joystick wykorzystany jako główny mechanizm sterowania planszą. Zasilany napięciem 3.3V z Raspberry Pi Pico, podłączony w następujący sposób:
- **VRx**: GP27 (ADC1)
- **VRy**: GP28 (ADC0)

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

### Plansza
Plansza, na której odbywa się rozgrywka.

---

## Schematy połączeń

### Schemat połączeń układu master

**Joystick ST1079:**
- GND → GND
- +5V → 3.3V
- VRx → GP27 (ADC1)
- VRy → GP26 (ADC0)

**Moduł Bluetooth HC-06:**
- Rx → GP17
- Tx → GP16
- GND → GND
- Vcc → Zewnętrzne źródło 5V

### Schemat połączeń układu slave

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

---

## Software
(Szczegóły implementacji oprogramowania, struktura kodu i instrukcje użytkowania do uzupełnienia.)

---
