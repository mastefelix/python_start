class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_asphalt_mass(self, weight=25, thickness=5):
        print(f'Масса асфальта - {int(self._length * self._width * weight * thickness / 1000)} тонн.')


road = Road(20, 5000)
road.full_asphalt_mass()
