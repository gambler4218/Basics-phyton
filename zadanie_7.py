from itertools import count
from math import factorial

def generator():
    for el in count(1):
        if el < 6:
        yield factorial(el)

fact = generator

for el in fact():
    print(el)
    break