def summation():
    result = 0
    while True:
        num_list = input("Введите строку чисел через пробел / q - выход \n")
        for i in num_list.split(" "):
            try:
                if i == "q":
                    print(f"Сумма чисел: {result}")
                    return result
                else:
                    result += int(i)
            except ValueError:
                print("Вы ввели что-то не то, введите строку чисел через пробел / q - выход")
        print(f"Сумма чисел: {result}")


summation()
