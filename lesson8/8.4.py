class Sklad:
    def __init__(self):
        self.dict = {}

    def add_to(self, equipment):
        self.dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class Equipment(Sklad):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return f'Model: {self.name}, year: {self.year}'


class Printer(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)


class Scaner(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)


class Xerox(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)


sklad = Sklad()
printer = Printer('HP', 2021)
sklad.add_to(printer)
scaner = Scaner('Canon', 2020)
sklad.add_to(scaner)
scaner = Scaner('Epson', 2020)
sklad.add_to(scaner)
(xerox) = Xerox('Xerox', 2019)
sklad.add_to(xerox)
print(sklad.dict)
