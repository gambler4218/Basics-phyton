n = int(input('Введите любое число больше 0: '))

while n > 0:
    if n >= 10 and n <=99:
        d = n // 10
        c = n % 10
        if d > c:
            print(d)
        elif c > d:
            print(c)
        break
    if n >= 100 and n <= 999:
        a = n // 100
        b = n // 10 % 10
        c = n % 10
        if c < a > b:
            print(a)
        elif a < c > b:
            print(c)
        elif a < b > c:
            print(b)
        break
else:
    print('Такого числа нет') # Если делать дальше то очень громоздко