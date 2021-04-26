def user():
    name = input('Введите Ваше имя:  ')
    surname = input('Введите Вашу фамилию: ')
    year = int(input('Введите год рождения: '))
    city = input('Введите Ваш город: ')
    email = input('Введите Вашу электронную почту: ')
    phone = int(input('Введите номер телефона: '))
    print(f'name - {name}, surname - {surname}, year - {year}, city - {city}, email - {email}, phone - {phone}')

print(user())