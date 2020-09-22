my_file = open("text_2.txt", "r", encoding="utf-8")
line = my_file.readlines()
lines = 0
for i in line:
    print(i)
    lines += 1
    i_str = i.split()
    print(f"Количество слов в строке {lines} - {len(i_str)}")
print(f"Количество строк в файле {lines}")

