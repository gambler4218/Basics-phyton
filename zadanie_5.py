class Stationery:
    title = None
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Писать ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Писать карандашом')
class Handle(Stationery):
    def draw(self):
        print('Выделить маркером')
stat = Stationery()
stat.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()