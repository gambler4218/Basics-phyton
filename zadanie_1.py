my_list = []
while True:
    user = input('Введите данные: ')
    if user == ' ':
        break
    else:
        line = user + '\n'
        my_list.append(line)

with open('doc.txt', 'w', encoding='utf-8') as my_file:
    my_file.writelines(my_list)