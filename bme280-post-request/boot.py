# boot.py -- run on boot-up
import network, time
from machine import Pin

led = Pin("LED", Pin.OUT)

# Replace the following with your WIFI Credentials
SSID = "pfe-insper"
SSI_PASSWORD = ""

def do_connect(timer=None):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        led.value(0)
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    led.value(1)
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()