import math

number = float(input("Введите число: "))
divided_number = math.modf(number)
print("Первое число дробной части:", math.floor(divided_number[0] * 10))
