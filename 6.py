a = int(input("Введите значение а: \n"))
b = int(input("Введите значение b: \n"))
count_days = 1
while True:
    if a < b:
        a = a + (a * 10 / 100)
        count_days += 1
    else:
        print(f"на {count_days}-й день спортсмен достиг результата — не менее {b} км ")
        break
