"""Example script for reading the PS2 joystick using ADS1115."""

from time import sleep
from joystick import Joystick


joy = Joystick()

print("Press Ctrl+C to exit")
try:
    while True:
        x, y, pressed = joy.read()
        print(f"X: {x} | Y: {y} | Button: {pressed}")
        sleep(0.2)
except KeyboardInterrupt:
    print("\nExiting...")
