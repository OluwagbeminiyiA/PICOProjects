from machine import Pin
from time import sleep

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(13, Pin.OUT)

sleep(1)

print('ready')

while True:
    if pir.value() > 0.5:
        print('Motion Detected')
        led.on()
        sleep(0.5)
    else:
        led.off()
        print("No motion detected")
        