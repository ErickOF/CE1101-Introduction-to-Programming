#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Erick Andres Obregon Fonseca
Copyright: Copyright 2023, CE1101-Introduction-to-Programming
Credits: Erick Andres Obregon Fonseca
License: MIT
Version: 1.0.0
Maintainer: Erick Andres Obregon Fonseca
Email: erickobregonf@gmail.com,erickof@ieee.org,erickof@estudiantec.cr
Status: Development

Description:
    In a Python script, declare, initialize, and display with the print function at least one
    variable with each type seen in this presentation.

Usage:
    $python convert_base_16_to_10.py
"""

__author__ = "Erick Andres Obregon Fonseca"
__copyright__ = "Copyright 2023, CE1101-Introduction-to-Programming"
__credits__ = ["Erick Andres Obregon Fonseca"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erick Andres Obregon Fonseca"
__email__ = "erickobregonf@gmail.com,erickof@ieee.org,erickof@estudiantec.cr"
__status__ = "Development"



from typing import *


def check_valid_digits(number: str) -> bool:
    """Check that each digit is valid for base 16 (hexadecimal).

    Args:
        number (str): hexadecimal number to validate.

    Returns:
        bool: True if it's valid, False otherwise.
    """
    valid_chars: str = '0123456789abcdef'
    # Convert number to lower case
    number = number.lower()

    # Check that each char is valid
    if number[0] in valid_chars and number[1] in valid_chars and number[2] in valid_chars:
        return True
    else:
        return False

def convert_base_16_to_10(number: int) -> int:
    """Convert from base 16 (hexadecimal) to base 10.

    Args:
        number (int): 3 digits number to convert.

    Returns:
        int: number in base 10.
    """
    # Convert number to lower case
    number = number.lower()

    # Converted number
    base10: int = 0

    # First digit * 16**0
    if number[2].isdigit():
        base10 += int(number[2])
    else:
        base10 += ord(number[2]) - ord('a') + 10

    # Second digit * 16**1
    if number[1].isdigit():
        base10 += int(number[1]) * 16
    else:
        base10 += (ord(number[1]) - ord('a') + 10) * 16

    # Third digit * 16**2
    if number[0].isdigit():
        base10 += int(number[0]) * 256
    else:
        base10 += (ord(number[0]) - ord('a') + 10) * 256

    return base10

def get_input_num() -> str:
    """Get input number from terminal.

    Returns:
        str: 3 digits number and '' if not valid.
    """
    number: str = input('Enter a 3 digits number: ')

    # Check if the number has 3 digits
    if len(number) != 3:
        return ''
    else:
        return number


if __name__ == '__main__':
    # Get the number to convert
    number: str = get_input_num()

    # Validate that input number has 3 digits
    if number == '':
        print('Number must have 3 valid characters')
    # Validate that input number has valid characters
    elif not check_valid_digits(number):
        print('Valid characters are 0-9 and a-f.')
    else:
        print(convert_base_16_to_10(number))
