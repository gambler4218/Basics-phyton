from functools import reduce
spisok = [i for i in range(100, 1001) if i % 2 == 0]

print(spisok)

def my_func(el, el1):
    return el * el1

print(reduce(my_func,[i for i in range(100, 1001) if i % 2 == 0]))