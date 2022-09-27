import math

count_numbers = int(input("Введите количество цифр: "))
for index in range(count_numbers):
    number = float(input("Введите число: "))
    if number > 0:
        number = math.ceil(number)
        print("x =", number, "\t", "log(x) =", math.log(number))
    elif number < 0:
        number = math.floor(number)
        print("x =", number, "\t", "exp(x) =", math.exp(number))
    else:
        print("0 ни положительно, ни отрицательное число!")