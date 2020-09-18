from itertools import count, cycle


while True:
    try:
        a = int(input("Введите начальное значение: "))
        b = a + 27
        break
    except:
        ValueError: print("Вы ввели некорректные входные данные, попробуйте еще разок")
for el in count(a):
     if el > b:
        break
     else:
        print(el)

с = a
for el in cycle("qwerty"):
    if с > b:
        break
    print(el)
    с += 1
