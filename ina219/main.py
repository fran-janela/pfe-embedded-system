import machine
from ina import INA219
from time import sleep
from packages import logging

i2c_id = 1
i2c_scl = 19
i2c_sda = 18

i2c = machine.I2C(i2c_id, scl=machine.Pin(i2c_scl), sda=machine.Pin(i2c_sda), freq=400000)
ina = INA219(0.1, i2c)
ina.configure()


while True:
    print("Voltage: " + str(ina.voltage()))
    print("Current: ", str(ina.current()))
    print("Power: " + str(ina.power()))
    print("Shunt Voltage: " + str(ina.shunt_voltage()))
    sleep(10)