import machine
import functions.RGB_PWMduty as rgb_pwm

class RGBModule:
    def __init__(self, red_pin, green_pin, blue_pin, FREQ=5000):
        self.red_pin = machine.Pin(red_pin, machine.Pin.OUT)
        self.green_pin = machine.Pin(green_pin, machine.Pin.OUT)
        self.blue_pin = machine.Pin(blue_pin, machine.Pin.OUT)

        self.red = machine.PWM(self.red_pin)
        self.green = machine.PWM(self.green_pin)
        self.blue = machine.PWM(self.blue_pin)

        self.red.freq(FREQ)
        self.green.freq(FREQ)
        self.blue.freq(FREQ)

        self.set_color(255, 0, 0)

    def set_color(self, red, green, blue):
        red, green, blue = rgb_pwm.rgb_to_pwm_duty(red, green, blue)
        self.red.duty_u16(red)
        self.green.duty_u16(green)
        self.blue.duty_u16(blue)