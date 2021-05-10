class Road:
    _length = None
    _width = None
    massa = 25
    thickness = None
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        self.thickness = int(input('Введите количество слоев асфальта: '))
        a = (self._length * self._width * self.massa * self.thickness) / 1000
        print(f'Масса асфальта: {a} т')

road = Road(600, 4)
road.weight()