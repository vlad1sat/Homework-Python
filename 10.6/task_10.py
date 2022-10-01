length_hole = int(input("Введите длину ямы: "))
element_hole = ""
number = length_hole
for line in range(0, length_hole):
    for element_line in range(length_hole, 0, -1):
        if element_line >= number:
            element_hole += str(element_line)
        else:
            element_hole += '.'
    print(element_hole + element_hole[::-1])
    number -= 1
    element_hole = ""
