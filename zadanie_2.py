user = int(input('Введите продолжительность рабочего дня в секундах: '))
hours = user // 3600
minutes = user % 3600 // 60
second = user - hours * 3600 - minutes * 60
print(f'Ваше рабочее время составляет {hours}:{minutes}:{second}')
print('Ваше рабочее время составляет {0}:{1}:{2}'.format(hours, minutes, second))
print('Ваше рабочее время составляет %d:%d:%d' % (hours, minutes, second))