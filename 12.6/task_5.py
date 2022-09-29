def count_letters(text, found_number, found_symbol):
    count_found_number = 0
    count_found_symbol = 0
    for symbol in text:
        if symbol == found_number:
            count_found_number += 1
        if symbol == found_symbol:
            count_found_symbol += 1
    print("Количество цифр", str(found_number) + ":", count_found_number)
    print("Количество букв", str(found_symbol) + ":", count_found_symbol)


text = input("Введите текст: ")
found_number = input("Какую цифру ищем? ")
found_symbol = input("Какую букву ищем? ")
count_letters(text, found_number, found_symbol)
