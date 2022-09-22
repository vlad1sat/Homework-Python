count_numbers = 0
for index in range(10):
    number = int(input("Введите число: "))
    if number % 2 == 0 and number > 0:
        count_numbers += 1
print("Подходящие цифры: ", count_numbers)
