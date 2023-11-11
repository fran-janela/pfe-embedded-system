from modules.bme_module import BME280Module
import machine
import time

I2C_ID = 0
I2C_SCL = 21
I2C_SDA = 20
I2C_ADDRESS = 0x77

# Initialize BME280 module
bme = BME280Module(i2c_id=I2C_ID, i2c_scl=I2C_SCL, i2c_sda=I2C_SDA, i2c_address=I2C_ADDRESS)

# Get readings
while True:
    readings = bme.get_readings()
    print(readings)
    time.sleep(5)