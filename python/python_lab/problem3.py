#!/usr/bin/env python3

"""
    problem3.py - Guess word length 
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 01/05/2018
"""

def guess_length(string, guess):
    """
    Guess a string length.

    Params:
        string <str>: Input string
        guess <int>: Guess number for its length 

    Return:
        Int code:
            - 0 if it matches
            - 1 if it is greater
            - (-1) if it is lesser
            - 404 if input is not valid
    """
    if not isinstance(string, str):
        return 404

    if not isinstance(guess, int):
        return 404

    if len(string) == guess:
        return 0
    elif len(string) > guess:
        return 1
    else:
        return -1

if __name__ == '__main__':
    assert 0   == guess_length('hello world', 11)
    assert 1   == guess_length('hello world', 10)
    assert -1  == guess_length('hello world', 12)
    assert 404 == guess_length('hello world', '11')
    assert 404 == guess_length(12, 12)
    assert 404 == guess_length(12, '12')
    assert 404 == guess_length(True, 12)
    assert 404 == guess_length(12, True)
