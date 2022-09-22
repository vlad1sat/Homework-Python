deposit = int(input("Введите сумму дохода: "))
tax = 0
if deposit <= 10000:
    tax = deposit * 0.13
elif deposit <= 50000:
    tax = (deposit - 10000) * 0.2 + 1300
else:
    tax = (deposit - 50000) * 0.3 + 9300
print("Ваш налог на доход составляет:", tax)
