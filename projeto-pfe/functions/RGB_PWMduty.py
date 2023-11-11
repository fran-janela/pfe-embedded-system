def rgb_to_pwm_duty(red, green, blue):
    """
    Convert RGB values to PWM duty cycle values
    :param red: Red value
    :param green: Green value
    :param blue: Blue value
    :return: Tuple of duty cycle values
    """
    #PWM: 0-65535
    #RGB: 0-255

    red = int(red * 257)
    green = int(green * 257)
    blue = int(blue * 257)

    return (red, green, blue)