with open('zarplata.txt') as doc:
    price = []
    i = 0
    for line in doc:
        i += 1
        string = line.split()
        numb = int(string[1])
        price.append(numb)
        if numb < 20000:
            human = string[0]
    salary = round(sum(price) / i, 2)
    print(f'Оклад менее 20000 имеет {human}')
    print(f'Средний размер заработной платы составляет {salary}')