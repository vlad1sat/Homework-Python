count_negative_comments = 0
count_positive_comments = 0
while True:
    comment = int(input("Введите оценку: "))
    if 0 < comment <= 100:
        count_positive_comments += 1
    elif -100 <= comment < 0:
        count_negative_comments += 1
    elif comment == 0:
        break
    else:
        print("Некорректная оценка")
print("Кол-во положительных чисел:", count_positive_comments)
print("Кол-во отрицательных чисел:", count_negative_comments)
