def my_funk(x, y):
    return 1 / x ** abs(y)


print(my_funk(6, -2))


#########################################

def func2(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


xz = int(input("Введите число"))
yz = abs(int(input("Введите число")))
print(func2(xz, yz))
