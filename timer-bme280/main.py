from modules.bme_module import BME280Module
from machine import Pin, Timer, deepsleep
import time

I2C_ID = 1
I2C_SCL = 19
I2C_SDA = 18
I2C_ADDRESS = 0x77

def timer_callback(timer):
    global bme
    readings = bme.get_readings()
    print(readings)

# Initialize BME280 module
bme = BME280Module(i2c_id=I2C_ID, i2c_scl=I2C_SCL, i2c_sda=I2C_SDA, i2c_address=I2C_ADDRESS)

timer = Timer()
timer.init(period=5000, mode=Timer.PERIODIC, callback=timer_callback)

# Get readings
while True:
    pass