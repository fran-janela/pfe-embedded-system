from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
    print("toggle LED")
    sleep(1)