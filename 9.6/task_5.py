position = [8, 10]
while True:
    message = "[Программа]: Марсоход находится на позиции " + str(position[0]) + ", " + str(
        position[1]) + " введите команду: "
    command = input(message).upper()
    match command:
        case 'W':
            if position[1] >= 20:
                continue
            position[1] += 1
        case 'S':
            if position[1] <= 0:
                continue
            position[1] -= 1
        case 'A':
            if position[0] <= 0:
                continue
            position[0] -= 1
        case 'D':
            if position[0] >= 15:
                continue
            position[0] += 1
        case _:
            print("Некорректная команда!")
