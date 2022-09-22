start_line = int(input("Введите начало отрезка: "))
finish_line = int(input("Введите конец отрезка: "))
result = 0
count_point = 0
for point in range(start_line, finish_line + 1):
    if point % 3 == 0:
        result += point
        count_point += 1
print("Среднее арифметическое всех чисел из отрезка [" + str(start_line) + ";",
      str(finish_line) + "], кратных числу 3 равно", result / count_point)
