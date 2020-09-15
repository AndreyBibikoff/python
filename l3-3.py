while True:
    try:
        one = int(input("Введите первое число \n"))
        two = int(input("Введите второе число \n"))
        three = int(input("Введите третье число \n"))
        break
    except ValueError:
        print("Вы ввели некорректные данные")


def my_func(a, b, c):
    d = min(a, b, c)
    print(f"Сумма наибольших двух аргументов {a + b + c - d}")


my_func(one, two, three)
