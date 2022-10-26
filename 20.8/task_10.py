def my_zip(symbols, numbers):
    zip_dict = dict()
    for index in range(min(len(symbols), len(numbers))):
        zip_dict[symbols[index]] = numbers[index]
    for element_zip in zip_dict.items():
        print(element_zip)


user_str = input("Строка: ")
user_symbols = list(user_str)
user_numbers = [int(number) for number in tuple(input("Кортеж чисел:(через запятую): ").split(', '))]
my_zip(user_symbols, user_numbers)
