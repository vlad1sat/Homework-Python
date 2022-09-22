last_salary = 0
is_rise = True
for month in range(1, 11):
    message = "Введите свою зарплату за " + str(month) + " месяц: "
    salary = int(input(message))
    if salary <= last_salary:
        is_rise = False
    last_salary = salary
if is_rise:
    print("Ваша зарплата возрастает! ;)")
else:
    print("Ваша зарплата не всегда увеличивается с каждым месяцем! ;(")