import machine
from time import sleep

potPin = 28

myPot = machine.ADC(potPin)

greenLED = machine.Pin(15, machine.Pin.OUT)
yellowLED = machine.Pin(12, machine.Pin.OUT)
redLED = machine.Pin(10, machine.Pin.OUT)

while True:
    potValue = myPot.read_u16()
    voltage = (100 / 65_247) * potValue - (288 * 100 / 65_247)
    print(voltage)
    if voltage <= 74:
        sleep(.5)
        greenLED.value(1)
        redLED.value(0)
        yellowLED.value(0)
    elif 74 < voltage < 94:
        sleep(.5)
        greenLED.value(0)
        redLED.value(0)
        yellowLED.value(1)
    else:
        sleep(.5)
        greenLED.value(0)
        redLED.value(1)
        yellowLED.value(0)