text = input("Введите текст: ")
words = text.split()
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
print("Самое длинное слово, букв:", max_length)
