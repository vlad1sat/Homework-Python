def expand_number(number, limiter, message):
    num_count = 0
    temp = number
    while temp > 0:
        num_count += 1
        temp = temp // 10
    if num_count < limiter:
        print("В первом числе меньше " + message + " цифр.")
        return
    else:
        last_digit = number % 10
        first_digit = number // 10 ** (num_count - 1)
        between_digits = number % 10 ** (num_count - 1) // 10
        number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return number


def menu():
    first_number = int(input("Введите первое число: "))
    first_expand_number = expand_number(first_number, 3, "трех")
    if first_expand_number is None:
        return
    print('Изменённое первое число:', first_expand_number)
    second_number = int(input("\nВведите второе число: "))
    second_expand_number = expand_number(second_number, 4, "четырех")
    if second_expand_number is None:
        return
    print('Изменённое второе число:', second_expand_number)
    print('\nСумма чисел:', first_expand_number + second_expand_number)


menu()
