def factorial_number(n):
    factorial = 1
    for number in range(2, n + 1):
        factorial *= number
    return factorial


def pow_number(n, x):
    result = 1
    for index in range(1, n + 1):
        result = result * x
    return result


precision = float(input("Введите точность: "))
x = int(input("Введите икс: "))
ceil = 1
result = 0
n = 0
while abs(ceil) > precision:
    ceil = pow_number(-1, n) * (pow_number(x, (2 * n)) / factorial_number((2 * n)))
    result += ceil
    n += 1
print("Сумма ряда =", result)
