from machine import Pin
import time


sound_sensor = Pin(0, Pin.IN)
led = Pin(15, Pin.OUT)

print("Sound Sensor Ready")
while True:
    print(sound_sensor.value())
    if sound_sensor.value() == 1:
        print("Sound Detected")
        led.on()
    else:
        led.off()
        
    time.sleep(0.2)
        