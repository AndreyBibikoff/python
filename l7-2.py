from abc import ABC, abstractmethod
class dress(ABC):

    @abstractmethod
    def get_square_coat(self):
        return self.V / 6.5 + 0.5

    @abstractmethod
    def get_square_jacket(self):
        return self.H * 2 + 0.3

class Coat(dress):
    def __init__(self, V):
        self.V = V

    @property
    def get_square_coat(self):
        c = self.V / 6.5 + 0.5
        return round(c, 2)

    def get_square_jacket(self):
        pass

    def __str__(self):
        return f'Расход ткани на пальто: \n{self.get_square_coat}'

class Jacket(dress):
    def __init__(self, H):
        self.H = H

    def get_square_coat(self):
        pass

    @property
    def get_square_jacket(self):
        return self.H * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм: \n{self.get_square_jacket}'

c = Coat(4)
j = Jacket(3)
print(c)
print(j)
print(f'Общий расход ткани: \n{float(c.get_square_coat) + float(j.get_square_jacket)}')

