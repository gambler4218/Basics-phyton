def my_func(a, b, c):
    my_list = [a, b, c]
    z = min(my_list)
    d = a + b + c - z
    return d

print(my_func(10, 18, 4))