prise_chairs = []
for chair in range(3):
    prise_chairs.append(int(input("Введите стоимость стула: ")))
cost = sum(prise_chairs)
print(cost) if cost <= 10000 else print(cost - (cost / 10))
