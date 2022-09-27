number = int(input('Введите число: '))
print()
for line in range(number + 1):
    for column in range(number + 1):
        if column == line:
            print('^', end='')
        elif column == number - line:
            print('^', end='')
        else:
            print(' ', end='')
    print()
