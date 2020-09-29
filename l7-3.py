class Cell:
    def __init__(self, c):
        self.c = c

    def __str__(self):
        return f'{self.c * "*"}'

    def __add__(self, other):
        return Cell(self.c + other.c)

    def __sub__(self, other):
        return Cell(int(self.c - other.c))

    def __mul__(self, other):
        return Cell(int(self.c * other.c))

    def __truediv__(self, other):
        return Cell(round(self.c // other.c))

    def make_order(self, c_in_row):
        row = ""
        for i in range(int(self.c / c_in_row)):
            row += f'{"o" * c_in_row} \n'
        row += f'{"o" * (self.c % c_in_row)}'
        return row


cells_1 = Cell(12)
cells_2 = Cell(21)
sum_cells = cells_1.__add__(cells_2)

print(sum_cells.make_order(5))
