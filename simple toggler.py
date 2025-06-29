from machine import Pin
from time import sleep


led = Pin(12, Pin.OUT)

while True:
    led.toggle()
    sleep(1)