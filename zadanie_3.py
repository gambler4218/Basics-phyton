class Worker:
    name = None
    surname = None
    position = None
    wage = None
    bonus = None
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
class Positions(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def posit(self):
        return self.position
    def get_income(self):
        self._incom = {'wage': self.wage, 'bonus': self.bonus}
        return self._incom
manager = Positions('Petrov', 'Viktor', 'slesar', 500, 100)
print(manager.get_full_name(), manager.posit(), manager.get_income())