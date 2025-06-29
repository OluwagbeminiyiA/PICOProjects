from machine import Pin
from time import sleep

led = Pin(11, Pin.OUT)
led2 = Pin(9, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)


while True:
    if button.value():
        print('Button Pressed')
        print(button.value())
        led.toggle()
        sleep(0.2)
        led2.toggle()
        sleep(0.2)
              