message = input("Введите текст: ")
index = 0
for symbol in message:
    if symbol == "*":
        print("Символ '*' на", index + 1, "позиции.")
        exit()
    index += 1
print("Символа '*' не встретилось.")