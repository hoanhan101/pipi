#!/usr/bin/env python3

"""
    read_sensor.py - Read our temperature and humidity sensor.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/07/2018
"""

import RPi.GPIO as GPIO
import datetime
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
    Get temperature and humidity reading.

    Params:
        None

    Return:
        Tuple of temperature and humidity in float if valid.
        0, 0 if not.
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

    if temp_cr == check_crc8(temp_msb, temp_lsb) and hum_crc == check_crc8(hum_msb, hum_lsb):
        temp = convert_temperature_reading(temp_msb, temp_lsb)
        humd = convert_humidity_reading(hum_msb, hum_lsb)
        return temp, humd
    else:
        return 0, 0

def convert_temperature_reading(temp_msb, temp_lsb, mode='celsius'):
    """
    Convert temperature reading to decimal value.

    Params:
        temp_msb <int>: Temperature MSB
        temp_lsb <int>: Temperature LSB
        mode <str>    : Temperature in Celsius of Fahrenheit

    Return:
        Temperature value in float.
    """
    raw_temp = (temp_msb << 8) + temp_lsb

    if mode == 'celsius':
        temp = -45 + 175.0 * (raw_temp / ((2**16) - 1))
    else:
        temp = -49 + 315.0 * (raw_temp / ((2**16) - 1))

    return round(temp, 2)

def convert_humidity_reading(hum_msb, hum_lsb):
    """
    Convert humidity reading to decimal value.

    Params:
        hum_msb <int>: Humidity MSB
        hum_lsb <int>: Humidity LSB

    Return:
        Humidity value in float.
    """
    raw_hum = (hum_msb << 8) + hum_lsb

    hum = 100.0 * (raw_hum / ((2**16) - 1))

    return round(hum, 2)

def check_crc8(msb, lsb):
    """
    Calculate checksum CRC code for a given msb and lsb.

    Params:
        msb <int>: MSB
        lsb <int>: LSB

    Return:
        Hex value of CRC
    """
    buffer = [msb, lsb]
    polynomial = 0x31
    crc = 0xFF
    index = 0

    for index in range(0, len(buffer)):
        crc ^= buffer[index] # ^ means XOR
        for i in range(8, 0, -1):
            if crc & 0x80:
                crc = (crc << 1) ^ polynomial
            else:
                crc = (crc << 1)
    return hex(crc & 0xFF)

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

def write_to_file(filename, data):
    """
    Write data to file.

    Params:
        filename: Target filename
        data: Data to write

    Return:
        None
    """
    with open(filename, 'a') as output_file:
        print(data)
        output_file.write(data)

def read_from_file(filename):
    """
    Read from file.

    Params:
        filename: Target filename

    Return:
        None
    """
    with open(filename, 'r') as output_file:
        line = output_file.readline()
        data = line.split(',')
        while line:
            print(data)
            line = output_file.readline()

if __name__ == '__main__':
    # temp, humd = get_reading()
    # result = str(datetime.datetime.now()) + ',' + str(temp) + ',' + str(humd) + ',' + '\n'

    # while True:
        # write_to_file('test.txt', result)
        # time.sleep(15)

    # read_from_file('test.txt')
    # print(check_crc8(0xB1, 0xEF))
    # get_status()
    # time.sleep(0.015)
    # clear_status()
    # time.sleep(0.015)
    # soft_reset()
