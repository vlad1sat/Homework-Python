hours = int(input("Введите отработанные часы: "))
loan_balance = int(input("Введите остаток по кредиту: "))
cost_food = int(input("Введите траты на еду: "))
cost_money = (200 * hours / 2 ** 3) + hours
print("Часов хватает. Можно отдохнуть") if cost_money >= loan_balance + cost_food \
    else print("Часов не хватает. Придётся работать!")
