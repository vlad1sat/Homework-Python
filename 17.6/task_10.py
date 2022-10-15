import string


message = input("Введите сообщение: ").lower()
shift = int(input("Введите сдвиг: "))
correct_message = []
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэю"   # нет нормальной реализации алфавита с буквой ё :(
for symbol in message:
    if symbol in string.punctuation or symbol == ' ':
        correct_message.append(symbol)
        continue
    index = alphabet.index(symbol) + shift
    if index > len(alphabet):
        correct_message.append(alphabet[index - len(alphabet) - 1])
    else:
        correct_message.append(alphabet[index])

print("Зашифрованное сообщение:", "".join(correct_message))
