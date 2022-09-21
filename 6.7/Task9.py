mystery_number = int(input("Введите число, которое нужно угадать: "))
count_attempt = 0
while True:
    number = int(input("Введите число: "))
    if number > mystery_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
        count_attempt += 1
    elif number < mystery_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
        count_attempt += 1
    else:
        count_attempt += 1
        print("Вы угадали! Число попыток:", count_attempt)
