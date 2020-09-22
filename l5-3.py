my_file = open("text_3.txt", "r", encoding="utf-8")
lines = my_file.readlines()
firm_staff = 0
fot = 0


print("Вычисляем сотрудников с окладом менее 20 000 из файлика:")

for i in lines:
    staff = i.split()
    firm_staff += 1
    fot += float(staff[1])
    if float(staff[1]) < 20000:
        needy = f"{staff[0]} - {staff[1]}"
        print(needy)
salary = fot / firm_staff
print(f"Общий ФОТ сотрудников: {fot}")
print(f"Средня величина дохода на одного сотрудника {salary}")
