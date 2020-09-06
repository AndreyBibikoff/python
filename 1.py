# Регистрация
name = input("Регистрация на сайте. Пожалуйста, придумайте логин: \n")
age = int(input(f"Привет {name}, Сколько тебе лет? \n"))
location = input(f"Из какого ты города {name}? \n")
user_pass = input("Придумай пароль \n")

# Авторизация
print("Вход в профиль")
while True:
    bd_name = input("Введите логин: \n")
    if bd_name == name:
        print(f"Привет {name} ")
        break
    else:
        print("Пользователь с таким логином не зарегистрирован")
while True:
    bd_passwd = input("Введите пароль: \n")
    if bd_passwd == user_pass:
        print(f"{name} Вы успешно авторизировались")
        print(f"Профиль: \n Имя пользователя: {name} \n Возраст:  {age} \n Город: {location}")
        break
    else:
        print("Ошибочка, попробуйте еще раз")
