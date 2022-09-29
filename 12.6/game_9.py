import random


def rock_paper_scissors():
    user_command = int(input("Выберите действие: 0 - Ножницы, 1 - Бумага, 2 - Камень: "))
    computer_move = random.randint(0, 2)
    if user_command > 2 or user_command < 0:
        print("Некорректная программа!")
        rock_paper_scissors()
    elif user_command == computer_move:
        print("Ничья!")
    elif (computer_move == 0 and user_command == 1) or (computer_move == 1 and user_command == 2) \
            or (computer_move == 2 and user_command == 0):
        print("Проигрыш!")
    else:
        print("Выигрыш!")


def guess_the_number():
    min_length = int(input("Введите начало диапозона: "))
    max_length = int(input("Введите конец диапозона: "))
    if min_length > max_length:
        print("Бредовый диапозон!")
        guess_the_number()
    print("Условия работы: 1 — равно, 2 — больше, 3 — меньше. Угадывает число от", min_length, "до", max_length)
    while True:
        middle = (max_length + min_length) // 2
        message = "Твоё число равно, меньше или больше, чем число " + str(middle) + "? "
        command = int(input(message))
        match command:
            case 1:
                print("Твое число -", middle)
                break
            case 2:
                min_length = middle + 1
            case 3:
                max_length = middle - 1
            case _:
                print("Неверная инструкция!")


def main_menu():
    print("Добро пожаловать в игру!")
    while True:
        command = input("Выберите игру! 1 - \"Камень, ножницы, бумага\", 2 - \"Угадай число\", 0 - Выход из игры: ")
        match command:
            case '1':
                rock_paper_scissors()
            case '2':
                guess_the_number()
            case '0':
                break
            case _:
                print("Некорректная команда!")
    print("До скорых встреч!")


main_menu()
