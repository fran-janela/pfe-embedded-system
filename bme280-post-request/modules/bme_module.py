# import bme280 from packages folder
from packages import bme280
import machine
import math

class BME280Module:
    def __init__(self, i2c_id, i2c_scl, i2c_sda, i2c_address):
        self.i2c = machine.I2C(i2c_id, scl=machine.Pin(i2c_scl), sda=machine.Pin(i2c_sda), freq=400000)
        self.bme = bme280.BME280(i2c=self.i2c, address=i2c_address)
    def get_readings(self):
        '''
        Returns a dictionary with temperature, pressure, and humidity readings
        Every reading as a value and a mesure unit
        '''
        (temperature, pressure, humidity) = self.bme.values
        # Example: temperature = '25.0C'
        # Example: pressure = '1000.0hPa'
        # Example: humidity = '50.0%'

        # Values:
        t_value = float(temperature[:len(temperature)-1])
        p_value = float(pressure[:len(pressure)-3])
        h_value = float(humidity[:len(humidity)-1])

        # Units:
        t_unit = temperature[len(temperature)-1:]
        p_unit = pressure[len(pressure)-3:]
        h_unit = humidity[len(humidity)-1:]

        return {
            'temperature': {
                'value': t_value,
                'unit': t_unit
            },
            'pressure': {
                'value': p_value,
                'unit': p_unit
            },
            'humidity': {
                'value': h_value,
                'unit': h_unit
            }
        }

        
        