my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open('doc1.txt') as doc:
        spisok = []
        for line in doc:
            string = line.split(' - ')
            if string[0] in my_dict:
                numb = my_dict[string[0]]
                spisok.append(numb + ' - ' + string[1])
        print(spisok)
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    with open('number.txt', 'w', encoding='utf-8') as number:
        number.writelines(spisok)
except IOError:
    print("Произошла ошибка ввода-вывода!")