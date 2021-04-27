def delenie():
    numb1 = int(input('Введите число: '))
    numb2 = int(input('Введите число: '))
    try:
        result = numb1 / numb2
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    return result

print(delenie())