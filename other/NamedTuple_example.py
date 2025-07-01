#!/usr/bin/python3
from collections import namedtuple

fruit = namedtuple('fruit', 'count sort color')

apple = fruit(count=5, sort="Antonovka", color="yellow")
print(apple.count, apple.sort, apple. color)