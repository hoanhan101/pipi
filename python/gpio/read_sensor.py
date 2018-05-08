#!/usr/bin/env python3

"""
    read_sensor.py - Read our temperature and humidity sensor.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/07/2018
"""

import RPi.GPIO as GPIO
import time
import smbus

LED_PIN = 20
GPIO_IS_SETUP = False
DEVICE_ADDRESS = 0x44

bus = smbus.SMBus(1)

def setup_gpio():
    """
    Setup GPIO to BCM and LED_PIN.

    Params:
        None

    Return:
        None
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO_IS_SETUP = True

    print('GPIO is setup')

def led_on():
    """
    Turn on the LED.

    Params:
        None

    Return:
        None
    """
    if not GPIO_IS_SETUP:
        setup_gpio()

    GPIO.output(LED_PIN, 1)

    print('LED is ON')

def led_off():
    """
    Turn off the LED.

    Params:
        None

    Return:
        None
    """
    if not GPIO_IS_SETUP:
        setup_gpio()

    GPIO.output(LED_PIN, 0)

    print('LED is OFF')

def get_status():
    """
    Get register status.

    Params:
        None

    Return:
        None
    """
    bus.write_byte_data(DEVICE_ADDRESS, 0xF3, 0x2D)
    block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 3)
    print('Status MSB:', hex(block[0]))
    print('Status LSB:', hex(block[1]))

def clear_status():
    """
    Clear status.

    Params:
        None

    Return:
        None
    """
    bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0x41)

def soft_reset():
    """
    Do the soft reset.

    Param:
        None

    Return:
        None
    """
    bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0xA2)

if __name__ == '__main__':
    get_status()
    clear_status()
    time.sleep(1)
    soft_reset()
