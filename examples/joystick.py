"""Utility module to read a PS2 joystick using an ADS1115 ADC."""

from adafruit_ads1x15 import ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import board
import busio


class Joystick:
    """Represents a PS2 joystick connected via ADS1115."""

    def __init__(self, x_channel=ADS.P0, y_channel=ADS.P1):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(i2c)
        self.x_axis = AnalogIn(self.ads, x_channel)
        self.y_axis = AnalogIn(self.ads, y_channel)

    def read(self):
        """Return a tuple of (x_value, y_value)."""
        return self.x_axis.value, self.y_axis.value
