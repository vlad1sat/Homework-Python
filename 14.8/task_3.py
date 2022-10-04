def sum_elements_number(number):
    result = 0
    for symbol in number:
        result += int(symbol)
    return result


def length_number(number):
    return len(number)


number = input("Введите число: ")
sum_number = sum_elements_number(number)
print("Сумма чисел:", sum_number)
length = length_number(number)
print("Количество цифр в числе:", length)
print("Разность суммы и количества цифр:", sum_number - length)
