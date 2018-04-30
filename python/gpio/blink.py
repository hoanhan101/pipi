#!/usr/bin/env python3

"""
    blink.py - Blink the line
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 04/30/18
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

def blink_light(nums_time):
    for i in range(nums_time):
        GPIO.output(20, 1)
        time.sleep(0.25)
        GPIO.output(20, 0)
        time.sleep(0.25)
        print(i)

blink_light(10)
GPIO.cleanup()
