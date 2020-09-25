class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')

        if self.speed > 60:
            print(f'У {self.name} превышение скорости!')
        else:
            print(f'{self.name} не превышает скоростной режим')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')

        if self.speed > 40:
            print(f'У {self.name} превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не полицейская машина')


mitsubishi = SportCar(200, 'Черная', 'Mitsubishi Lancer Evo', False)
renault_logan = TownCar(30, 'Бежевый', 'Renault logan', False)
gazelle = WorkCar(60, 'Белая', 'Газель', False)
ford = PoliceCar(110, 'Серебристый', 'Ford', True)
mitsubishi.go()
mitsubishi.show_speed()
gazelle.go()
gazelle.show_speed()
gazelle.turn_left()
ford.go()
ford.police()
gazelle.stop()
ford.stop()
renault_logan.go()
renault_logan.show_speed()
