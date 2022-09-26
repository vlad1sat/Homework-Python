day_week = input("Введите день недели: ").lower()
week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота" "воскресенье"]
index = 0
for day in week:
    if day == day_week:
        print("Номер дня недели: " + str(index + 1))
        exit()
    index += 1
print("Некорректно введен день недели!")