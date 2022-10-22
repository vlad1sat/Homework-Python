message = input("Сообщение: ").split()
reversed_message = []
special_symbols = [',', '.', '!', '?']

for word in message:
    reversed_word = []
    for symbol in word:
        if symbol in special_symbols:
            reversed_word.append(symbol)
        else:
            reversed_word.insert(0, symbol)
    reversed_message.append(''.join(reversed_word))

print("Новое сообщение:", ' '.join(reversed_message))

