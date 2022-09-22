count_violations = 0
for zona in range(30, 36):
    message = "Людей в " + str(zona) + "-м секторе: "
    count_people = int(input(message))
    if count_people > 10:
        print("Нарушение! Слишком много людей в секторе!")
        count_violations += 1
    else:
        print("Всё спокойно.")
print("Количество нарушений:", count_violations)
