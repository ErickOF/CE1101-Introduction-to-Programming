#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Erick Andres Obregon Fonseca
Copyright: Copyright 2016, CE1101-Introduction-to-Programming
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
    $python exercise1.py
"""

__author__ = "Erick Andres Obregon Fonseca"
__copyright__ = "Copyright 2016, CE1101-Introduction-to-Programming"
__credits__ = ["Erick Andres Obregon Fonseca"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erick Andres Obregon Fonseca"
__email__ = "erickobregonf@gmail.com,erickof@ieee.org,erickof@estudiantec.cr"
__status__ = "Development"

from array import array
from typing import *

integer_num: int = 20
boolean: bool = False
real_num: float = 2.5
complex_num: complex = 5 + 3j
string: str = "Hello, World!"
tuple_type: Tuple[Any] = (0, 1, 2, 3, 4, 5)
immutable_bytearray: bytes = b'Immutable Byte Array'
list_type: List[Any] = [0, 1, 2, 4, 5]
array_type: array = array('i', [0, 1, 2, 3, 4, 5])
mutable_bytearray: bytearray = bytearray(b'Mutable Byte Array')
sets: Set[Any] = {0, 1, 2, 3, 4, 5}
immutable_set: frozenset = frozenset({0, 1, 2, 3, 4, 5})
dictionary: Dict[Any, Any] = {'hola': 'hello'}

print(integer_num, type(integer_num))
print(boolean, type(bool))
print(real_num, type(real_num))
print(complex_num, type(complex_num))
print(string, type(string))
print(tuple_type, type(tuple_type))
print(immutable_bytearray, type(immutable_bytearray))
print(list_type, type(list_type))
print(array_type, type(array_type))
print(mutable_bytearray, type(mutable_bytearray))
print(sets, type(sets))
print(immutable_set, type(immutable_set))
print(dictionary, type(dictionary))
