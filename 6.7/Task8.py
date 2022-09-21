sum_deposit = int(input("Начальная сумма вклада: "))
sum_desired = int(input("Желаемая сумма вклада: "))
percent = int(input("Процент вклада: "))
years = 0
while sum_deposit < sum_desired:
    sum_deposit += sum_deposit * percent // 100
    years += 1
print(years)
