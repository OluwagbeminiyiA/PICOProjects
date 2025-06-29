import ahtx0
from machine import Pin, I2C
from time import sleep

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
sensor = ahtx0.AHT10(i2c)

led = Pin(12, Pin.OUT)

while True:
    print("Temperature: ", sensor.temperature, "Humidity: ", sensor.relative_humidity)
    sleep(0.5)
    if sensor.temperature > 27:
        print("It's getting warm in here")
        led.on()
    led.off()
        