def check_coordinate(coordinate_x, coordinate_y, radius):
    return coordinate_x ** 2 + coordinate_y ** 2 <= radius ** 2


print("Введите координаты монетки: ")
coordinate_x = float(input("X: "))
coordinate_y = float(input("Y: "))
radius = float(input("Введите радиус: "))
if check_coordinate(coordinate_x, coordinate_y, radius):
    print("Монетка где-то рядом.")
else:
    print("Монетки в области нет.")