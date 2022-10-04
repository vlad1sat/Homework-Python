def expand_number(number):
    result = ""
    for symbol in range(len(number) - 1, -1, -1):
        if number[symbol] == '0' and result == "":
            continue
        result += number[symbol]
    return int(result)


def menu():
    first_number = input("Введите первое число: ")
    second_number = input("Введите второе число: ")
    expand_first_number = expand_number(first_number)
    expand_second_number = expand_number(second_number)
    print("Первое число наоборот:", expand_first_number)
    print("Второе число наоборот:", expand_second_number)
    sum_numbers = expand_first_number + expand_second_number
    print("Сумма:", sum_numbers)
    print("Сумма наоборот:", expand_number(str(sum_numbers)))


menu()
