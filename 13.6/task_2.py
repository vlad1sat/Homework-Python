def get_max(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


first_number = int(input("Введите число: "))
second_number = int(input("Введите число: "))
third_number = int(input("Введите число: "))
print("Самое большое число", get_max(get_max(first_number, second_number), third_number))
