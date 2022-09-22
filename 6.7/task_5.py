str_number = input("Введите номер билета: ")
first_sum = 0
second_sum = 0
if len(str_number) % 2 == 1:
    print("Несчастливый билет")
    exit()
for first_number in range(0, len(str_number) // 2):
    first_sum += int(str_number[first_number])
for second_number in range(len(str_number) // 2, len(str_number)):
    second_sum += int(str_number[second_number])
if first_sum == second_sum:
    print("Счастливый билет")
else:
    print("Несчастливый билет")
