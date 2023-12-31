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
