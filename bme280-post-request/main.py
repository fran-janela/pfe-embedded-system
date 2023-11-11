from modules.bme_module import BME280Module
from machine import Pin, Timer, deepsleep
import time
import network, json
import urequests as request
from boot import do_connect

I2C_ID = 1
I2C_SCL = 19
I2C_SDA = 18
I2C_ADDRESS = 0x77

def request_timer_callback(timer):
    global bme
    readings = bme.get_readings()
    print(readings)
    data = json.dumps({
        "sensor_id": 1,
        "temperature": readings["temperature"]["value"],
        "temperature_unit": readings["temperature"]["unit"],
        "pressure": readings["pressure"]["value"],
        "pressure_unit": readings["pressure"]["unit"],
        "humidity": readings["humidity"]["value"],
        "humidity_unit": readings["humidity"]["unit"]
    })
    r = request.post("http://10.168.167.33:8800/sensor/measure/", data=data, headers = {'Content-type': 'application/json'})
    print(r.text)
    print("Request sent! Going to sleep...")

# Initialize BME280 module
bme = BME280Module(i2c_id=I2C_ID, i2c_scl=I2C_SCL, i2c_sda=I2C_SDA, i2c_address=I2C_ADDRESS)

# Initialize request timer
request_timer = Timer()
request_timer.init(period=20000, mode=Timer.PERIODIC, callback=request_timer_callback)

# Initialize conectivity verification timer
connectivity_timer = Timer()
connectivity_timer.init(period=120000, mode=Timer.PERIODIC, callback=do_connect)

do_connect()

# Get readings
while True:
    pass