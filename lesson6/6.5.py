class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Рисуем {self.title}!')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}!')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}!')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}!')


pen = Pen('шариковая ручка')
pencil = Pencil('мягкий карандаш')
handle = Handle('черный маркер')
draw = [pen, pencil, handle]
for i in draw:
    i.draw()
