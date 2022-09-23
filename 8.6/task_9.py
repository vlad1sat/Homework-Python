x = int(input("Введите x: "))
numerator = 1
denominator = 1
for index in range(1, 7):
    element_1 = (x - (2 ** index - 1))
    numerator *= element_1
    element_2 = (x - 2 ** index)
    denominator *= element_2
if denominator == 0:
    print("Деление на 0!")
else:
    print(numerator / denominator)
