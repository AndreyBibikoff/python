while True:
    try:
        a = int(input("Введите первое целое число"))
        b = int(input("Введите второе целое число"))
        break
    except ValueError:
        print("Вы ввели не целое число, а что-то другое, попробуйте еще раз")


def my_def(var1, var2):
    try:
        result = var1 / var2
        print(f"Результат - {result}")
    except ZeroDivisionError:
        print("На 0 делить нельзя")


my_def(a, b)
