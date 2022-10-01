uncorrected_word = input("Введите зашифрованное слово: ")
correct_word = ""
for index in range(0, len(uncorrected_word) // 2):
    correct_word += uncorrected_word[index] + uncorrected_word[len(uncorrected_word) - index - 1]
if len(uncorrected_word) % 2 == 1:
    correct_word += uncorrected_word[len(uncorrected_word) // 2]
print("Расшифрованное слово:", correct_word)
