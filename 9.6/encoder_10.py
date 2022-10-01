word = input("Введите слово, которое нужно защифровать: ")
encoded_word = ""
for index in range(0, len(word) // 2):
    encoded_word += word[index] + word[len(word) - index - 1]
if len(word) % 2 == 1:
    encoded_word += word[len(word) // 2]
print("Зашифрованное слово:", encoded_word)
