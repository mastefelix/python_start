from time import sleep


class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN']

    def running(self):
        while True:
            print(f'\r\033[31m{self.__color[0]}', end='')
            sleep(7)
            print(f'\r\033[33m{self.__color[1]}', end='')
            sleep(2)
            print(f'\r\033[32m{self.__color[2]}', end='')
            sleep(7)
            print(f'\r ', end='')
            sleep(0.5)
            print(f'\r\033[32m{self.__color[2]}', end='')
            sleep(0.5)
            print(f'\r ', end='')
            sleep(0.5)
            print(f'\r\033[32m{self.__color[2]}', end='')
            sleep(0.5)
            print(f'\r ', end='')
            sleep(0.2)
            print(f'\r\033[33m{self.__color[1]}', end='')
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
