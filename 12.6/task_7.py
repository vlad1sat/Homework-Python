def min_number():
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    print("Наименьшее число:", (first_number + second_number - abs(first_number - second_number)) / 2)


min_number()
