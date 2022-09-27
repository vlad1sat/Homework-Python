result = 0
length_factorial = int(input("Сумма факториалов до числа N включительно: "))
if length_factorial == 0:
    print("Результат равен:", result + 1)
    exit()
for number in range(1, length_factorial + 1):
    factorial = 1
    for factorial_number in range(1, number + 1):
        factorial *= factorial_number
    result += factorial
print("Результат равен:", result)
