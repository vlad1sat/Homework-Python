length_list = int(input("Введите длину списка: "))

result = [number % 5 if number % 2 != 0 else 1 for number in range(length_list)]

print("Результат:", result)
