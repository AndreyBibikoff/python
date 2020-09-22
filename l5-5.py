my_file = open("text_5.txt", 'w', encoding="utf-8")
a = my_file.write(input("Введите числа через пробел: \n"))
my_file.close()
my_file = open("text_5.txt", 'r', encoding='utf=8')
b = my_file.read()
print(f"Считываем числа из файла: {b}")
pars_lst = b.split(" ")
try:
    result = 0
    for i in pars_lst:
        result += int(i)
    print(f"Сумма чисел в файле: {result}")
except ValueError:
    print("Ошибка, нужно ввети числа!")






