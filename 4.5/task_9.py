mileage = input("Введите пробег: ")
day = int(input("Введите сегодняшнее число: "))
sum_mileage = 0
for number in mileage:
    sum_mileage += int(number)
if sum_mileage > day:
    print("Сброс.")
    print("Пробег: 0")
else:
    print("Сегодня не сломался.")
    print("Пробег:", mileage)
