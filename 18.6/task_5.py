while True:
    password = input("Придумайте пароль: ")
    count_numbers = 0
    is_upp = False

    if len(password) >= 8:
        for symbol in password:
            if symbol.isdigit():
                count_numbers += 1
            if symbol.isupper():
                is_upp = True

    if count_numbers >= 3 and is_upp:
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")