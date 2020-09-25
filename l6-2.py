class Road:
    _length = None
    _width = None

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def build(self):
        self.weigth = 25
        self.tickness = 5
        need = self._length * self._width * self.weigth * self.tickness / 1000
        print(f"Необходимая масса асфальта {need} тонн")


building = Road(5000, 20)
building.build()
