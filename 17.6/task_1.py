correct_symbols = ['а', 'е', 'у', 'о', 'и', 'я', 'ы', 'э', 'ё', 'ю']
message = input("Введите текст: ")

result = [symbol for symbol in message if symbol in correct_symbols]
print(result)
print("Длинна списка:", len(result))
