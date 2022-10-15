count_number = int(input('Кол-во чисел: '))
numbers = []
add_numbers = []
for _ in range(count_number):
    numbers.append(int(input('Число: ')))

print("Последовательность:", numbers)

index = 0
while numbers != numbers[::-1]:
    numbers.insert(count_number, numbers[index])
    add_numbers.append(numbers[index])
    index += 1

print('Нужно приписать чисел:', index)
print('Сами числа:', add_numbers)