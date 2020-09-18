from functools import reduce


def my_funk(prev_el, el):
    return prev_el * el


print(reduce(my_funk, [el for el in range(100, 1001) if el % 2 == 0]))
