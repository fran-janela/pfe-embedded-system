from machine import Pin
import time

# Pin 22 is the optoisolator
relay = Pin(22, Pin.OUT)
onboard_led = Pin("LED", Pin.OUT)

# Reset relay GPIO
relay.value(0)
onboard_led.value(0)

while(True):
    relay.toggle()
    onboard_led.toggle()
    time.sleep(1)
