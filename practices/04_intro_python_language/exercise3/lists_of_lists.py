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
    Implement a list of lists, where the first list contains the start and end
    times of the theoretical class, and the second list the start and end
    times of the workshop class.

Usage:
    $python lists_of_lists.py
"""

from typing import *

__author__ = "Erick Andres Obregon Fonseca"
__copyright__ = "Copyright 2023, CE1101-Introduction-to-Programming"
__credits__ = ["Erick Andres Obregon Fonseca"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erick Andres Obregon Fonseca"
__email__ = "erickobregonf@gmail.com,erickof@ieee.org,erickof@estudiantec.cr"
__status__ = "Development"


classes: List[List[int]] = [
    # Theorical class [start, end]
    [730, 930],
    # Workshop class [start, end]
    [930, 1130]
]

