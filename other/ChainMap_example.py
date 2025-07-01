#!/usr/bin/python3
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'b': 4}

dict = ChainMap(dict1, dict2)

print(dict)