class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {sum(self._income.values())}')


emloyee_1 = Position('Иван', 'Петров', 'курьер', 20000, 10000)
emloyee_1.get_full_name()
print(emloyee_1.position)
emloyee_1.get_total_income()
emloyee_2 = Position('Петр', 'Иванов', 'охранник', 15000, 5000)
emloyee_2.get_full_name()
print(emloyee_2.position)
emloyee_2.get_total_income()
