import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from gpiozero import LED

from UltrasonicSensor import UltrasonicSensor

GPIO.setmode(GPIO.BCM)  # Use physical pin numbering

