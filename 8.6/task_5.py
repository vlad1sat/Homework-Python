start_line = int(input("Введите начало отрезка: "))
finish_line = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))
if step < 0:
    start_line, finish_line = finish_line, start_line - 1
else:
    finish_line += 1
for point in range(start_line, finish_line, step):
    result = point ** 3 + 2 * point ** 2 - 4 * point + 1
    print("В точке", point, "функция равна", result)
