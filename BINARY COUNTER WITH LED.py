from machine import Pin
from time import sleep

LED = Pin(15, Pin.OUT)
LED2 = Pin(11, Pin.OUT)
LED3 = Pin(7, Pin.OUT)
LED4 = Pin(3, Pin.OUT)

value1 = 0
value2 = 0
value3 = 0
value4 = 0

i = 0
while i < 16:
    LED.value(i % 2)
    LED2.value((i >> 1) % 2)
    LED3.value((i >> 2) % 2)
    LED4.value((i >> 2) // 2)
    i += 1
    sleep(1)
    

LED.value(0)
LED2.value(0)
LED3.value(0)
LED4.value(0)

