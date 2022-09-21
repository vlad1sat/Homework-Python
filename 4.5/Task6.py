cube_kostya = int(input("Кубик Кости: "))
cube_owner = int(input("Кубик владельца: "))
if cube_owner > cube_kostya:
    print("Сумма:", cube_kostya + cube_owner)
    print("Владелец платит")
else:
    print("Сумма:", cube_kostya - cube_owner)
    print("Костя платит")
print("Игра окончена!")
