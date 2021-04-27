def my_func(x, y):
    a = x ** y
    return a

print(my_func(2, -3))


def my_func_1(x, y):
    i = 0
    while i >= y:
        result = x ** y
        i -= 1
    return result
print(my_func_1(4, -2))