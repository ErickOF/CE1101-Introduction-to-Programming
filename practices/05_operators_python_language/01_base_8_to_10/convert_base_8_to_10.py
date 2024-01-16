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
    Write a program that passes a 3-digit number from base 8 (octal) to base
    10.

Usage:
    $python convert_base_8_to_10.py
"""

__author__ = "Erick Andres Obregon Fonseca"
__copyright__ = "Copyright 2023, CE1101-Introduction-to-Programming"
__credits__ = ["Erick Andres Obregon Fonseca"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erick Andres Obregon Fonseca"
__email__ = "erickobregonf@gmail.com,erickof@ieee.org,erickof@estudiantec.cr"
__status__ = "Development"



def check_valid_digits(num: int) -> bool:
    """Check that each digit is valid for base 8 (octal).

    Args:
        num (int): num to validate.

    Returns:
        bool: True if it's valid, False otherwise.
    """
    if ((num % 10) > 7) or (((num // 10) % 10) > 7) or (((num // 100) % 10) > 7):
        return False
    else:
        return True

def convert_base_8_to_10(num: int) -> int:
    """Convert from base 8 (octal) to base 10.

    Args:
        num (int): 3 digits num to convert.

    Returns:
        int: num in base 10.
    """
    # Converted num
    ## First digit * 8**0
    base10: int = num % 10
    num //= 10
    ## Second digit * 8**1
    base10 += (num % 10) * 8
    num //= 10
    ## Third digit * 8**2
    base10 += (num % 10) * 64

    return base10

def get_input_num() -> int:
    """Get input number from terminal.

    Returns:
        int: 3 digits number or -1 if an invalid number is given.
    """
    num: int = int(input('Enter a 3 digits number: '))

    # Check if the number has 3 digits
    if 100 < abs(num) < 999:
        return num
    else:
        return -1


if __name__ == '__main__':
    # Get the number to convert
    number: int = get_input_num()

    # Validate that input number has 3 digits
    if number == -1:
        print('Number must have 3 digits')
    # Validate that input number has digits between 0 and 7
    elif not check_valid_digits(number):
        print('Number must have digits between 0 and 7.')
    else:
        print(convert_base_8_to_10(number))
