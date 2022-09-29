def summa_n(end_number):
    sum_number = 0
    for number in range(1, end_number + 1):
        sum_number += number
    print("Я знаю, что сумма чисел от 1 до", end_number, "равна", sum_number)


number = int(input("Введите число: "))
summa_n(number)
