class Worker:
    name = None
    surname = None
    position = None
    _income = {'profit': 0, 'bonus': 0}

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        self._income = {'profit': self.profit, 'bonus': self.bonus}
        return self._income['profit'] + self._income['bonus']


manager = Position('Mark', 'Zukerberg', 'software engineer', 5000, 1500)
fullname = manager.get_full_name()
prof = manager.get_total_income()
print(f'{fullname} - Total income: {prof}')
