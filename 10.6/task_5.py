count_numbers = int(input("Введите кол-во чисел: "))
result = 0
for index in range(count_numbers):
    number = int(input("Введите число: "))
    dividers = 0
    for divider in range(1, number + 1):
        if number % divider == 0:
            dividers += 1
    if dividers == 2:
        result += 1
print("Количество простых чисел в последовательности:", result)
