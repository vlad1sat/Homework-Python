cost = int(input("Введите стоимость квартиры(млн.): "))
square = int(input("Введите площадь квартиры(м^2): "))
if (cost < 10 and square > 100) or (cost < 7 and square > 80):
    print("Квартира вам подходит!")
else:
    print("Квартира вам не подходит!")
