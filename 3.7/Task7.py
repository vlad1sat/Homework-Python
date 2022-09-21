speed = int(input("Введите скорость (км/ч): "))
hours = int(input("Введите время (ч): "))
distance = speed * hours
while distance > 115:
    distance -= 115
print(distance)
