from sys import argv

print('Введите количество часов, оплату за час и размер премии')

hours, payment, prize = argv

print('Зарплата: ', (hours * payment + prize))