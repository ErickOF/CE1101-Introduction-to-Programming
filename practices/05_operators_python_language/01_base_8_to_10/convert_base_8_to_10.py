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



from typing import *


def convert_base_8_to_10(number: int) -> int:
    """Convert from base 8 (octal) to base 10.

    Args:
        number (int): 3 digits number to convert.

    Returns:
        int: number in base 10.
    """
    # Converted number
    ## First digit * 8**0
    base10: int = (number % 10)
    number //= 10
    ## Second digit * 8**1
    base10 += (number % 10) * 8
    number //= 10
    ## Third digit * 8**2
    base10 += (number % 10) * 64

    return base10

def get_input_num() -> int:
    """Get input number from terminal.

    Returns:
        int: 3 digits number or -1 if an invalid number is given.
    """
    number: int = int(input('Enter a 3 digits number: '))

    # Check if the number has 3 digits
    if 100 < abs(number) < 999:
        return number
    else:
        return -1


if __name__ == '__main__':
    # Get the number to convert
    number: int = get_input_num()

    # Validate if input number is valid
    if number == -1:
        print('Number must have 3 digits')
    else:
        print(convert_base_8_to_10(number))
