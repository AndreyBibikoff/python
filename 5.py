receipt = int(input("Введите размер выручки\n"))
cost = int(input("Введите размер издержек\n"))

if receipt > cost:
    profit = (receipt - cost)
    print(f"Фирма сработала с прибылью: {profit:.2f} монеток")
    print(f"Рентабельность выручки составляет {profit / receipt * 100:.0f} %")
    staff = int(input("Введите количество сотрудников \n"))
    staff_profit = (profit / staff)
    print(f"Прибыль на одного сотрудника составляет: {staff_profit:.2f} монеток")
elif cost > receipt:
    profit = (receipt - cost)
    print(f"Фирма сработала с в убыток: {profit:.2f} монеток")
else:
    print("Фирма сработала в 0")
