def anketa(name, surname, birthday, city, email, tel):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {birthday}, Город проживания: {city}, "
          f"Электронная почта: {email}, Телефон: {tel}")


anketa(name=input("Введите Имя \n"), surname=input("Введите Фамилию \n"), birthday=input("Введите год рождения \n"),
       city=input("Введите город проживания \n"), email=input("Введите электронную почту \n"),
       tel=input("Введите телефон \n"))
