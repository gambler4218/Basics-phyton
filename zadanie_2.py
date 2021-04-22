user = list(input('Введите данные: '))

if len(user) % 2 == 0:
    user[::2], user[1::2] = user[1::2], user[::2]
elif len(user) % 2 != 0:
    i = 0
    while i < len(user) - 1:
        user[i], user[i+1] = user[i+1], user[i]
        i +=2
print(user)