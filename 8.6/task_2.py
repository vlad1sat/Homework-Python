count_debtors = int(input("Введите количество должников: "))
sum_debtors = 0
for debtor in range(0, count_debtors, 5):
    print("Должник с номером", debtor)
    sum_debtors += int(input("Сколько должны? "))
print("Общая сумма долга:", sum_debtors)
