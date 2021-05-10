class Car:
    speed = None
    colour = None
    name = None
    is_police = False

    def __init__(self, name, colour, speed, is_police):
        self.name = name
        self.colour = colour
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return (f'The car {self.name} go with {self.speed} km/h')
    def stop(self):
        return 'The car stop'
    def turn(self, side):
        return 'The car turn' + ' ' + side
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, name, colour, speed, is_police):
        super().__init__(self, name, colour, speed)
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'  #не знаю почему не работает

class SportCar(Car):
    def __init__(self, name, colour, speed, is_police):
        super().__init__(self, name, colour, speed)
class WorkCar(Car):
    def __init__(self, name, colour, speed, is_police):
        super().__init__(self, name, colour, speed)
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости' #не знаю почему не работает
class PoliceCar(Car):
    def __init__(self, name, colour, speed):
        super().__init__(self, name, colour, speed)

town = TownCar('Subaru', 'red', 80, False)
print(town.go())
sport = SportCar('Subaru', 'red', 80, False)
work = WorkCar('Subaru', 'red', 80, False)
police = PoliceCar('Subaru', 'red', 80)