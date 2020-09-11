user_list = input("Введите значения списка через пробел \n")
lst = list(user_list.split())
print(f"Список до обработки {lst}")
tmp = 0
for i in range(int(len(lst) / 2)):
    lst[tmp], lst[tmp + 1] = lst[tmp + 1], lst[tmp]
    tmp += 2
print(f"Список после обработки {lst}")
