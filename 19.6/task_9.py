count_people = int(input("Введите количество человек: "))

data = dict()
for index in range(1, count_people):
    descendant, parent = input(f"{index} пара: ").split()
    if data.get(parent):
        data[parent].append(descendant)
    else:
        data[parent] = [descendant]

print(data)