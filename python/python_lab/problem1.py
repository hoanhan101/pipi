#!/usr/bin/env python3

"""
    problem1.py - Add, substract, multiply and divide two numbers
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 01/05/2018
"""

def add_two_numbers(num1, num2):
    """
    Add two numbers.

    Params:
        num1 <int>/<float>: Number 1
        num2 <int>/<float>: Number 2

    Return:
        Sum of two numbers:
            - in int if two numbers are int
            - in float if two numbers are float
            - 0 if input is not valid
    """
    if isinstance(num1, int) or isinstance(num1, float):
        if isinstance(num2, int) or isinstance(num2, float):
            return num1 + num2
        return 0
    return 0

def substract_two_numbers(num1, num2):
    """
    Substract two numbers.

    Params:
        num1 <int>/<float>: Number 1
        num2 <int>/<float>: Number 2

    Return:
        Difference of two numbers: 
            - in int if two numbers are int
            - in float if two numbers are float
            - 0 if input is not valid
    """
    if isinstance(num1, int) or isinstance(num1, float):
        if isinstance(num2, int) or isinstance(num2, float):
            return num1 - num2
        return 0
    return 0


def multiply(num, times):
    """
    Multiply a number by a number of times.

    Params:
        num <int>/<float>: Number to multiply
        times <int>: Number of times to multiply

    Return:
        Product of a number:
            - in int if the number is int
            - in float if the number is float
            - 0 if input is not valid
    """
    if not isinstance(times, int):
        return 0

    if isinstance(num, int) or isinstance(num, float):
        total = 0
        for i in range(times):
            total += num
        return total
    return 0

def divide(num, times):
    """
    Divide a number by a number of times.

    Params:
        num <int>/<float>: Number to divide
        times <int>: Number of times to divide

    Return:
        Quotient of a number: 
            - in int if the number is int or float
            - 0 if input is not valid
    """
    if num == 0:
        return 0

    if times == 1:
        if isinstance(num, int) or isinstance(num, float):
            return num
        return 0
    
    if not isinstance(times, int):
        return 0

    if num < times:
        return 0
    
    counter = -1
    while num >= 0:
        num -= times
        counter += 1

    return counter
    
    return 0

if __name__ == '__main__':
    # Test addition
    assert 10    == add_two_numbers(5, 5)
    assert -10   == add_two_numbers(-5,-5)
    assert 10.0  == add_two_numbers(5.0, 5.0)
    assert -10.0 == add_two_numbers(-5.0, -5.0)
    assert 10.0  == add_two_numbers(5, 5.0)
    assert 10.0  == add_two_numbers(5.0, 5)
    assert 0     == add_two_numbers('', 5)
    assert 0     == add_two_numbers(5, '')
    assert 0     == add_two_numbers('', '')

    # Test subtraction
    assert 0     == substract_two_numbers(5, 5)
    assert 0     == substract_two_numbers(-5,-5)
    assert -10   == substract_two_numbers(-5, 5)
    assert 10    == substract_two_numbers(5, -5)
    assert 0.0   == substract_two_numbers(5.0, 5.0)
    assert 0.0   == substract_two_numbers(-5.0, -5.0)
    assert -10.0 == substract_two_numbers(-5.0, 5.0)
    assert 10.0  == substract_two_numbers(5.0, -5.0)
    assert 0.0   == substract_two_numbers(5, 5.0)
    assert 0.0   == substract_two_numbers(5.0, 5)
    assert 0     == substract_two_numbers('', 5)
    assert 0     == substract_two_numbers(5, '')
    assert 0     == substract_two_numbers('', '')

    # Test multiplication
    assert 25    == multiply(5, 5)
    assert -25   == multiply(-5, 5)
    assert 27.5  == multiply(5.5, 5)
    assert -27.5 == multiply(-5.5, 5)
    assert 0     == multiply(5, '')
    assert 0     == multiply('', 5)
    assert 0     == multiply('', '')
    assert 0     == multiply(5, '5')
    assert 0     == multiply('', 5)
    assert 0     == multiply(5.5, 5.5)

    # Test division
    assert 0     == divide(0, 5)
    assert 0     == divide(0, 1)
    assert 5     == divide(5, 1)
    assert 5.0   == divide(5.0, 1)
    assert 2     == divide(10, 5)
    assert 2     == divide(11, 5)
    assert 0     == divide(5, 10)
    assert 2     == divide(10.0, 5)
    assert 2     == divide(10.5, 5)
    assert 2     == divide(11.5, 5)
