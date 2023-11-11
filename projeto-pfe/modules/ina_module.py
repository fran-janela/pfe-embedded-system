# import bme280 from packages folder
import ina
import machine
import math

class INA219Module:
    def __init__(self, i2c_id, i2c_scl, i2c_sda, i2c_address=0x40):
        self.i2c = machine.I2C(i2c_id, scl=machine.Pin(i2c_scl), sda=machine.Pin(i2c_sda), freq=400000)
        self.ina = ina.INA219(0.1, self.i2c)
        self.ina.configure()

    def get_readings(self):
        '''
        Returns a dictionary with voltage, current, and power readings
        Every reading as a value and a mesure unit
        '''
        voltage = self.ina.voltage()
        current = self.ina.current()
        power = self.ina.power()

        return {
            'voltage': {
                'value': voltage,
                'unit': 'V'
            },
            'current': {
                'value': current,
                'unit': 'mA'
            },
            'power': {
                'value': power,
                'unit': 'mW'
            }
        }
        