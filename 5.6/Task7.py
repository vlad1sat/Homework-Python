numbers = []
for number in range(3):
    numbers.append(int(input("Введите число: ")))
if numbers[0] == numbers[1] == numbers[2]:
    print("3 числа совпадают.")
elif numbers[0] == numbers[1] or numbers[1] == numbers[2] or numbers[0] == numbers[2]:
    print("2 числа совпадают.")
else:
    print("0 чисел совпадают.")
