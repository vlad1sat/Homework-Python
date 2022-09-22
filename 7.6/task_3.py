sum_salary = 0
for month in range(1, 13):
    message = "Введите зарплату за " + str(month) + " месяц: "
    sum_salary += int(input(message))
print("Средняя зарплата за год:", sum_salary / 12)
