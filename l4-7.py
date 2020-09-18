def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


n1 = int(input("Введите число\n"))
for el in fact(n1):
    b = el
print(f"Факториал {n1} = {b}")
