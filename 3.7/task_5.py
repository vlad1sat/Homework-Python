minutes = int(input("Введите количество минут: "))
hours = minutes // 60
minutes %= 60
print("Количество часов:", str(hours) + ",", "количество минут:", minutes)
