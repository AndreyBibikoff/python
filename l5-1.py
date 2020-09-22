new_f = open("text1.txt", "w")
while True:
    content = (input("Введите данные в файл, либо оставьте строку пустой и нажмите 'Enter' для завершения: \n"))
    if content == "":
        break
    new_f.write(f"{content}\n")
new_f.close()
