# работает с любым количеством чисел
def sum_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def def_max(numbers):
    return max(numbers)


def def_min(numbers):
    return min(numbers)


while True:
    accepted_values = input("Введите числа через пробел: ").split()
    numbers = [int(element) for element in accepted_values]
    if len(numbers) == 0:
        print("Некорректный ввод!")
        continue
    command = int(input("Введите команду, которую нужно сделать с цифрами: "
                        "0 - сложение, 1 - найти максимальное, 2 - найти минимальное: "))
    match command:
        case 0:
            print("Сумма цифр равна:", sum_numbers(numbers))
        case 1:
            print("Максимальное число:", def_max(numbers))
        case 2:
            print("Минимальное число:", def_min(numbers))
        case '_':
            print("Некорректная команда!")
