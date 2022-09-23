attempt = 0
min_length = 1
max_length = 100
print("Условия работы: 1 — равно, 2 — больше, 3 — меньше. Угадывает число от 1 до 100 за max 7 шагов! :)")
while attempt < 7:
    middle = (max_length + min_length) // 2
    message = "Твоё число равно, меньше или больше, чем число " + str(middle) + "? "
    command = int(input(message))
    match command:
        case 1:
            print("Твое число -", middle)
            exit()
        case 2:
            min_length = middle + 1
        case 3:
            max_length = middle - 1
        case _:
            print("Неверная инструкция!")
            attempt -= 1
    attempt += 1
print("Вы перезагадали число! ;)")
