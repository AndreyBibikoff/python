from random import randint

gen_l = [randint(1, 20) for i in range(1, 15)]
new_l = []
print(gen_l)
for i in range(len(gen_l) - 1):
    if gen_l[i] < gen_l[i + 1]:
        new_l.append(gen_l[i + 1])
print(f"Список до обработки {gen_l}")
print(f"Список после обработки {new_l}")
