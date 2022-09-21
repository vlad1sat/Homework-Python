count_months = 0
while True:
    day = int(input("Введите число дней в месяце: "))
    if day == 0:
        break
    if day % 2 == 0:
        count_months += 1
print("Количество четных месяцев:", count_months)
