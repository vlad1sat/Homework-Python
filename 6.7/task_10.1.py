# Немного усовершенствованный алгоритм для поиска числа в
min_length = int(input("Введите начало диапозона: "))
max_length = int(input("Введите конец диапозона: "))
if min_length > max_length:
    exit("Бредовый диапозон! Пока!")
print("Условия работы: 1 — равно, 2 — больше, 3 — меньше. Угадывает число от", min_length, "до", max_length)
while True:
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
