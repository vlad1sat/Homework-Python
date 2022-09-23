end_range = int(input("Введите конец последовательности: "))
result = 0
for n in range(0, end_range + 1):
    result += ((-1) ** n) * (1 / (2 ** n))
print("Результат:", result)
