def int_func(user_str):
    res = list(user_str)
    for i in res:
        if ord(i) == 32 or ord(i) in range(97, 123):
            res1 = user_str.title()
            print(res1)
            return res1
        else:
            print("Вы ввели некорректное значение, нужна строка из маленьких латинских букв же")
            break


int_func(user_str=input("Введите строку из маленьких латинских букв: \n"))
