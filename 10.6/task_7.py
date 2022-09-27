count_numbers = int(input("Введите количество чисел: "))
max_sum_number = 0
max_number = 0
for index in range(count_numbers):
    number = input("Введите число: ")
    sum_number = 0
    for symbol in number:
        sum_number += int(symbol)
    if sum_number > max_sum_number:
        max_sum_number = sum_number
        max_number = int(number)
print("Наибольшее число по сумме цифр:", max_number, end='. ')
print("Его сумма:", max_sum_number)
