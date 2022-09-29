def search_point():
    coordinate_x = float(input("Введите координату x: "))
    coordinate_y = float(input("Введите координату y: "))
    if -1 <= coordinate_x <= 1 and -1 <= coordinate_y <= 1:
        print("Точка в области!")
    else:
        print("точка не в области!")


search_point()