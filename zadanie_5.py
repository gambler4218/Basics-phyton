try:
    spisok = []
    with open('summa_number.txt', 'w', encoding='utf-8') as number:
        user = input('Введите любые числа через пробел: ')
        number.write(user)
        numb = user.split()
        for i in numb:
            a = int(i)
            spisok.append(a)
        print(sum(spisok))

except IOError:
    print("Произошла ошибка ввода-вывода!")