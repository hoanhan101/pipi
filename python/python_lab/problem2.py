#!/usr/bin/env python3

"""
    problem2.py - Get total ASCII value of all characters in a given string
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 01/05/2018
"""

def get_total_ascii(string):
    """
    Get total ASCII value of all characters in a given string.

    Params:
        string <str>: Input string

    Return:
        Total of the ASCII value in int. 0 if input is not valid.
    """
    if not isinstance(string, str):
        return 0

    total = 0
    for char in string:
        total += ord(char)

    return total

if __name__ == '__main__':
    assert 1116 == get_total_ascii('hello world')
    assert 733  == get_total_ascii('hoanhan')
    assert 146  == get_total_ascii('101')
    assert 0    == get_total_ascii('')
    assert 0    == get_total_ascii(0)
    assert 0    == get_total_ascii(1.0)
    assert 0    == get_total_ascii(True)
