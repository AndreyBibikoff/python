user_time = int(input("Введите время в секундах: \n"))

hours = (user_time // 3600)
balace = (user_time % 3600)
minutes = (balace // 60)

print(f"{hours:02}:{minutes:02}:{balace % 60:02}")
