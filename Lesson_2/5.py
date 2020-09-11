rating = [7, 6, 6, 4, 3, 3, 1]
print(f"Изначальный рейтинг: \n {rating}")
new_key = int(input("Введите рейтинг \n"))

for i, el in reversed(list(enumerate(rating))):
    if el == new_key:
        rating.insert(i + 1, new_key)
        break
    elif rating[0] < new_key:
        rating.insert(0, new_key)
        break
    elif rating[-1] > new_key:
        rating.append(new_key)
        break
    elif el > new_key < el + 1:
        rating.insert(i + 1, new_key)
        break
print(f"Обновленный рейтинг: \n {rating}")


# Как по мне так тоже решение согласоно ТЗ)):

user_rating = int(input("Введите значение рейтинга \n"))
rating.insert(0, user_rating)
rating.sort(reverse=True)
print(rating)
