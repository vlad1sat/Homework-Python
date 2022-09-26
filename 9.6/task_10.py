# НЕ РЕШЕНА пока что



# ....
uncorrected_word = input("Введите зашифрованное слово: ")
correct_word = ""
length_word = len(uncorrected_word)
for first_index in range(0, length_word, 2):
    correct_word += uncorrected_word[first_index]
if length_word % 2 == 1:
    correct_word += uncorrected_word[length_word // 2 ]
    length_word -= 2
for second_index in range(length_word - 1, 0, -2):
    correct_word += uncorrected_word[second_index]
print("Расшифрованное слово:", correct_word)
