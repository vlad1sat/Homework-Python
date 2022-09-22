position = int(input("Введите место в списке поступающих: "))
if position > 10:
    print("К сожалению, вы не поступили.")
    exit()
message = "Поздравляем, вы поступили!"
points = int(input("Введите количество баллов за экзамены: "))
if points < 290:
    print(message)
    print("Но вам не хватило баллов для стипендии.")
else:
    print(message)
    print("Бонусом вам будет начисляться стипендия.")
