height_pyramid = int(input("Введите высоту пирамиды: ")) + 3
for floor in range(1, height_pyramid, 2):
    middle_floor = (height_pyramid - floor) // 2
    print(' ' * middle_floor + '#' * floor + ' ' * middle_floor)
