first_list = []
second_list = []

for index in range(3):
    number = int(input(f"Введите {index + 1} число для первого списка: "))
    first_list.append(number)

for index in range(7):
    number = int(input(f"Введите {index + 1} число для второго списка: "))
    second_list.append(number)

print("Первый список:", first_list)
print("Второй список:", second_list)

first_list.extend(second_list)
for _ in range(len(first_list)):
    for index in first_list:
        if first_list.count(index) > 1:
            first_list.remove(index)

print("Новый первый список с уникальными элементами:", first_list)
