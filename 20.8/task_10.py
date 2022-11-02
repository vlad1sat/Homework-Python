def my_zip(symbols, numbers):
    return ((symbols[index], numbers[index]) for index in range(min(len(symbols), len(numbers))))


user_str = input("Строка: ")
user_symbols = list(user_str)
user_numbers = [int(number) for number in tuple(input("Кортеж чисел:(через запятую): ").split(', '))]
zip_user = my_zip(user_symbols, user_numbers)
print(zip_user)
for element_zip in zip_user:
    print(element_zip)