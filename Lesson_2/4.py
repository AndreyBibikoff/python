user_str = input("Введите предложение из нескольких слов \n")

list_user_str = user_str.split(" ")

for ind, el in enumerate(list_user_str):
    print(ind + 1, el[0:10])
