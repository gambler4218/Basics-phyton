my_list = [7, 5, 3, 3, 2]
user = int(input('Введите число: '))
c = my_list.count(user)

for n in my_list:
    if c > 0:
        i = my_list.index(user)
        my_list.insert(i + 1, user)
        break
    else:
        if n < user:
            i = my_list.index(n)
            my_list.insert(i, user)
            break
        elif n > user:
            my_list.append(user)
            break
print(my_list)