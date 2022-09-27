width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for line in range(height + 1):
    for column in range(width + 1):
        if column == 0 or column == width:
            print('|', end='')
        elif line == 0 or line == height:
            print('-', end='')
        else:
            print(' ', end='')
    print()
