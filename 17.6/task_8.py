count_sticks = int(input("Количество палок: "))
coordinates = []
area = ['|' for _ in range(count_sticks)]
count_throws = int(input("Количество бросков: "))

for throw in range(count_throws):
    message = "Сбиты палки с номера"
    coordinates.append(int(input("Сбиты палки с номера ")) - 1)
    coordinates.append(int(input("по номер ")))
    for index in range(coordinates[0], coordinates[1]):
        area[index] = '.'
    coordinates.clear()

print("".join(area))
