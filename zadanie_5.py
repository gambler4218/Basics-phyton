revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите сумму издержек: '))

if revenue > costs:
    print('Фирма приносит прибыль')
    profit = revenue - costs
    rentab = profit / revenue * 100
    print(f'Рентабельность составляет {rentab}%')
    people = int(input('Введите количество сотрудников: '))
    profit_people = profit / people
    print(f'На одного сотрудника приходится {profit_people} от общей прибыли')
else:
    print('Фирма приносит одни убытки')