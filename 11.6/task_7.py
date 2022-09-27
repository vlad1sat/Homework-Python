print("Введите местоположение коня: ")
x1 = int(float(input()) * 10)
y1 = int(float(input()) * 10)
print("Введите местоположение точки на доске: ")
x2 = int(float(input()) * 10)
y2 = int(float(input()) * 10)
print("Конь в клетке (" + str(x1) + "," + str(y1) + "). Точка в клетке (" + str(x2) + "," + str(y2) + ").")
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь может ходить в эту точку.")