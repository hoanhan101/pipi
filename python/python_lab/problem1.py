#!/usr/bin/env python3

"""
    problem1.py - Add and multiply two numbers
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
        Sum of two numbers in int or float. 0 if not valid.
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
        Difference of two numbers in int or float. 0 if not valid.
    """
    if isinstance(num1, int) or isinstance(num1, float):
        if isinstance(num2, int) or isinstance(num2, float):
            return num1 - num2
        return 0
    return 0


def multiply(num, times):
    """
    Multiple a number by a number of times.

    Params:
        num <int>/<float>: Number to multiply
        times <int>: Number of times to multiply

    Return:
        Product in int or float. 0 if not valid.
    """
    if not isinstance(times, int):
        return 0

    if isinstance(num, int) or isinstance(num, float):
        total = 0
        for i in range(times):
            total += num
        return total
    return 0

def divide(num1, times):
    """
    """
    if num1 == 0:
        return 0

    if times == 1:
        if isinstance(num1, int) or isinstance(num1, float):
            return num1
        return 0

if __name__ == '__main__':
    # Test addition
    assert 10   == add_two_numbers(5, 5)
    assert 10.0 == add_two_numbers(5.0, 5.0)
    assert 10.0 == add_two_numbers(5, 5.0)
    assert 10.0 == add_two_numbers(5.0, 5)
    assert 0    == add_two_numbers('', 5)
    assert 0    == add_two_numbers(5, '')
    assert 0    == add_two_numbers('', '')

    # Test subtraction
    assert 0    == substract_two_numbers(5, 5)
    assert 0.0  == substract_two_numbers(5.0, 5.0)
    assert 0.0  == substract_two_numbers(5, 5.0)
    assert 0.0  == substract_two_numbers(5.0, 5)
    assert 0    == substract_two_numbers('', 5)
    assert 0    == substract_two_numbers(5, '')
    assert 0    == substract_two_numbers('', '')

    # Test multiplication
    assert 25   == multiply(5, 5)
    assert 27.5 == multiply(5.5, 5)
    assert 0    == multiply(5, '')
    assert 0    == multiply('', 5)
    assert 0    == multiply('', '')
    assert 0    == multiply(5, '5')
    assert 0    == multiply('', 5)
    assert 0    == multiply(5.5, 5.5)

    # Test division
    assert 0    == divide(0, 5)
    assert 0    == divide(0, 1)
    assert 5    == divide(5, 1)
    assert 5.0  == divide(5.0, 1)
    # assert 2    == divide(10, 5)
    # assert 0    == divide(5, 10)
    # assert 0.5  == divide(5.0, 10.0)
