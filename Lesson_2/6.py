p_tuple = tuple()
product_list = []
product_dict = {}
product_analytics = {}
n = 1
while True:
    a = input("Ввод нового товара. Enter - продолжить / q - выход \n")
    if a == "q":
        break
    product_dict['Название'] = input("введите название: ")
    product_dict['Цена'] = input("Стоимость: ")
    product_dict['Количество'] = input("Количество: ")
    product_dict['ед'] = input("единицу измерения: ")
    product_list.append((n, product_dict))
    n += 1

print(product_list)
