from random import choice


class Car:
    way = ['прямо', 'налево', 'направо', 'назад']

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начала движение.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self):
        print(f'{self.name} движется {choice(self.way)}.')

    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed}. Превышение!' \
            if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} едет со скоростью: {self.speed}. Превышение!' \
            if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super(PoliceCar, self).__init__(name, speed, color, is_police=True)


town_car = TownCar('Lexus', 80, 'зеленый')
work_car = WorkCar('Камаз', 30, 'оранжевый')
sport_car = SportCar('Mazda', 150, 'красный')
police_car = PoliceCar('УАЗ', 80, 'белый')

list_of_cars = [town_car, work_car, sport_car, police_car]
for i in list_of_cars:
    i.go()
    i.turn()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
