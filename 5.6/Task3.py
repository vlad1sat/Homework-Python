element_x = int(input("Введите икс: "))
message = "Игрек равен:"
if element_x > 0:
    print(message, element_x - 12)
elif element_x == 0:
    print(message, 5)
else:
    print(message, element_x ** 2)
