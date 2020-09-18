from random import randint

gen_list = [randint(1, 12) for i in range(1, 15)]
new = []
print(gen_list)
for i in range(len(gen_list)):
    for el in range(len(gen_list)):
        if i != el and gen_list[i] == gen_list[el]:
            break
    else:
        new.append(gen_list[i])
print(new)