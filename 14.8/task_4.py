def reversed_number(exponent, mantissa):
    return exponent[::-1] + "." + mantissa[::-1]


first_number = input("Введите первое число: ")
elements_number = first_number.split('.')
reversed_first_number = reversed_number(elements_number[0], elements_number[1])
second_number = input("Введите второе число: ")
elements_number = second_number.split('.')
reversed_second_number = reversed_number(elements_number[0], elements_number[1])
print("Первое число наоборот:", reversed_first_number)
print("Второе число наоборот:", reversed_second_number)
print("Сумма:", float(reversed_first_number) + float(reversed_second_number))
