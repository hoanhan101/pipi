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
    time.sleep(0.015)
    block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 3)
    print('Status MSB:', hex(block[0]))
    print('Status LSB:', hex(block[1]))

def get_reading():
    """
    TODO

    Params:
        None

    Return:
        None
    """
    bus.write_byte_data(DEVICE_ADDRESS, 0x24, 0x00)
    time.sleep(0.015)
    block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 6)

    temp_msb = block[0]
    temp_lsb = block[1]
    temp_crc = block[2]
    hum_msb  = block[3]
    hum_lsb  = block[4]
    hum_crc  = block[5]

    convert_temperature_reading(temp_msb, temp_lsb)
    convert_temperature_reading(temp_msb, temp_lsb, 'fahrenheit')
    convert_humidity_reading(hum_msb, hum_lsb)

    print(hex(temp_crc), hex(hum_crc))

def convert_temperature_reading(temp_msb, temp_lsb, mode='celsius'):
    """
    Convert temperature reading to decimal value.

    Params:
        temp_msb <int>: Temperature MSB
        temp_lsb <int>: Temperature LSB
        mode <str>    : Temperature in Celsius of Fahrenheit

    Return:
        None
    """
    raw_temp = (temp_msb << 8) + temp_lsb

    if mode == 'celsius':
        temp = -45 + 175.0 * (raw_temp / ((2**16) - 1))
    else:
        temp = -49 + 315.0 * (raw_temp / ((2**16) - 1))

    print(str(round(temp, 2)))

def convert_humidity_reading(hum_msb, hum_lsb):
    """
    Convert humidity reading to decimal value.

    Params:
        hum_msb <int>: Humidity MSB
        hum_lsb <int>: Humidity LSB

    Return:
        None

    """
    raw_hum = (hum_msb << 8) + hum_lsb

    hum = 100.0 * (raw_hum / ((2**16) - 1))

    print(str(round(hum, 2)))

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
    get_reading()
    # get_status()
    # time.sleep(0.015)
    # clear_status()
    # time.sleep(0.015)
    # soft_reset()
