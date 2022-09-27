height_pyramid = int(input('Введите количество уровней пирамиды: '))
number = 1

for line in range(1, height_pyramid + 1):
    print('\t' * (height_pyramid - line), end='')
    for column in range(line):
        print(number, end='')
        number += 2
        print('\t' * 2, end='')
    print()
