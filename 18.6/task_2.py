words = input("Введите строку: ").split()
big_word = ""

for word in words:
    if len(word) > len(big_word):
        big_word = word

print("Самое длинное слово:", big_word)
print("Длина этого слова:", len(big_word))
