from modules.ina_module import INA219Module
from modules.bme_module import BME280Module
from modules.rgb_module import RGBModule
from modules.wifi_test_module import WIFITestModule
from modules.send_module import SendModule
from time import sleep
import json
import gc

SSID = "pfe-insper"
SSID_PASSWORD = ""

ina_i2c_id = 1
ina_i2c_scl = 19
ina_i2c_sda = 18

bme_12c_id = 0
bme_12c_scl = 21
bme_12c_sda = 20

wifi_led_red_pin = 4
wifi_led_green_pin = 3
wifi_led_blue_pin = 2

sensor_led_red_pin = 8
sensor_led_green_pin = 7
sensor_led_blue_pin = 6

server_ip = "10.168.167.33:8800"
server_get_url = "http://" + server_ip + "/"
server_send_url = "http://" + server_ip + "/sensor/measure/"

ina = INA219Module(ina_i2c_id, ina_i2c_scl, ina_i2c_sda)
bme = BME280Module(bme_12c_id, bme_12c_scl, bme_12c_sda, 0x77)

wifi_rgb = RGBModule(wifi_led_red_pin, wifi_led_green_pin, wifi_led_blue_pin)
sensor_rgb = RGBModule(sensor_led_red_pin, sensor_led_green_pin, sensor_led_blue_pin)

wifiTest = WIFITestModule(SSID, SSID_PASSWORD, "")
send = SendModule(server_send_url)

if wifiTest.sta_if.isconnected():
    wifi_rgb.set_color(0, 0, 255)

if len(ina.i2c.scan()) > 0 or len(bme.i2c.scan()) > 0:
    sensor_rgb.set_color(0, 0, 255)

if len(ina.i2c.scan()) > 0 and len(bme.i2c.scan()) > 0:
    sensor_rgb.set_color(0, 255, 0)


while True:
    ## Getting readings
    ina_readings = ina.get_readings()
    bme_readings = bme.get_readings()
    if wifiTest.sta_if.isconnected():
        internet_readings = wifiTest.test_internet_speed_conection()
    else:
        wifi_rgb.set_color(255, 0, 0)
        wifiTest.establish_connection()
        wifi_rgb.set_color(0, 0, 255)

    ## Printing readings
    # print("Voltage: " + str(ina_readings["voltage"]["value"]) + " " + ina_readings["voltage"]["unit"])
    # print("Current: " + str(ina_readings["current"]["value"]) + " " + ina_readings["current"]["unit"])
    # print("Power: " + str(ina_readings["power"]["value"]) + " " + ina_readings["power"]["unit"])
    # print("Temperature: " + str(bme_readings["temperature"]["value"]) + " " + bme_readings["temperature"]["unit"])
    # print("Pressure: " + str(bme_readings["pressure"]["value"]) + " " + bme_readings["pressure"]["unit"])
    # print("Humidity: " + str(bme_readings["humidity"]["value"]) + " " + bme_readings["humidity"]["unit"])
    # if internet_readings != {"error": "No internet connection"}:
    #     print("Internet ping: " + str(internet_readings["ping"]["value"]) + " " + internet_readings["ping"]["unit"])
    #     print("Internet speed: " + str(internet_readings["speed"]["value"]) + " " + internet_readings["speed"]["unit"])
    # else:
    #     print("No internet connection")
    # if intranet_readings != {"error": "No intranet connection"}:
    #     print("Intranet ping: " + str(intranet_readings["ping"]["value"]) + " " + intranet_readings["ping"]["unit"])
    #     print("Intranet speed: " + str(intranet_readings["speed"]["value"]) + " " + intranet_readings["speed"]["unit"])
    # else:
    #     print("No intranet connection")
    
    ## Displaying LEDs
    print("DEBUG: Displaying LEDs...")
    if internet_readings != {"error": "No internet connection"}:
        print("DEBUG: internet_readings != {'error': 'No internet connection'}")
        wifi_rgb.set_color(0, 255, 0)
    elif wifiTest.sta_if.isconnected():
        wifi_rgb.set_color(0, 0, 255)
    else:
        wifi_rgb.set_color(255, 0, 0)
        wifiTest.establish_connection()

    print("DEBUG: ina_i2c.scan(): " + str(len(ina.i2c.scan())))
    print("DEBUG: bme_i2c.scan(): " + str(len(bme.i2c.scan())))

    if len(ina.i2c.scan()) > 0 and len(bme.i2c.scan()) > 0:
        sensor_rgb.set_color(0, 255, 0)
    elif len(ina.i2c.scan()) > 0 or len(bme.i2c.scan()) > 0:
        sensor_rgb.set_color(0, 0, 255)
    else:
        sensor_rgb.set_color(255, 0, 0)


    ## Sending data
    print("DEBUG: Sending data...")
    if internet_readings != {"error": "No internet connection"}:
        data = json.dumps({
            "sensor_id": 1,
            "temperature": bme_readings["temperature"]["value"],
            "temperature_unit": bme_readings["temperature"]["unit"],
            "humidity": bme_readings["humidity"]["value"],
            "humidity_unit": bme_readings["humidity"]["unit"],
            "pressure": bme_readings["pressure"]["value"],
            "pressure_unit": bme_readings["pressure"]["unit"],
            "voltage": ina_readings["voltage"]["value"],
            "voltage_unit": ina_readings["voltage"]["unit"],
            "current": ina_readings["current"]["value"],
            "current_unit": ina_readings["current"]["unit"],
            "power": ina_readings["power"]["value"],
            "power_unit": ina_readings["power"]["unit"],
            "internet_ping": internet_readings["ping"]["value"],
            "internet_ping_unit": internet_readings["ping"]["unit"],
            "internet_speed": internet_readings["speed"]["value"],
            "internet_speed_unit": internet_readings["speed"]["unit"]
        })
    else:
        data = json.dumps({
            "sensor_id": 1,
            "temperature": bme_readings["temperature"]["value"],
            "temperature_unit": bme_readings["temperature"]["unit"],
            "humidity": bme_readings["humidity"]["value"],
            "humidity_unit": bme_readings["humidity"]["unit"],
            "pressure": bme_readings["pressure"]["value"],
            "pressure_unit": bme_readings["pressure"]["unit"],
            "voltage": ina_readings["voltage"]["value"],
            "voltage_unit": ina_readings["voltage"]["unit"],
            "current": ina_readings["current"]["value"],
            "current_unit": ina_readings["current"]["unit"],
            "power": ina_readings["power"]["value"],
            "power_unit": ina_readings["power"]["unit"],
            "internet_ping": 0.0,
            "internet_ping_unit": "No internet connection",
            "internet_speed": 0.0,
            "internet_speed_unit": "No internet connection"
        })

    try:
        result = send.send_data(data)
        print(result.text)
        result.close()
    except Exception as e:
        print(e)
        print("Error sending data")

    gc.collect()
    sleep(10)