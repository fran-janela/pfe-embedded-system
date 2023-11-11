import network
import urequests as requests
from functions.wifi_connection import do_connect

import time

class WIFITestModule():
    def __init__(self, SSID, SSID_PASSWORD, test_server_url):
        self.SSID = SSID
        self.SSID_PASSWORD = SSID_PASSWORD
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.test_server_url = test_server_url
        self.establish_connection()

    def establish_connection(self):
        do_connect(self.SSID, self.SSID_PASSWORD, self.sta_if)


    def test_internet_speed_conection(self):
        try:
            start_time = time.ticks_ms()  # Using ticks_ms for time measurement
            response = requests.get("https://www.google.com")
            response.close()  # Close the response to free memory
            end_time = time.ticks_ms()
            size = 53248 / 1000  # KB
            time_elapsed = (end_time - start_time) / 1000  # Convert milliseconds to seconds
            speed = size / time_elapsed
            return {
                'ping': {
                    'value': time_elapsed,
                    'unit': 's'
                },
                'speed': {
                    'value': speed,
                    'unit': 'KB/s'
                }
            }
        except Exception as e:
            print(e)
            return {"error": "No internet connection"}