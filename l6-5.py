class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


draw_pen = Pen()
draw_pencil = Pencil()
draw_handle = Handle()
draw_pen.draw()
draw_pencil.draw()
draw_handle.draw()
