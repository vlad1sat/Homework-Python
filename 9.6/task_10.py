uncorrected_word = input("Введите зашифрованное слово: ")
count_iteration = 0
left_part = ""
right_part = ""
for symbol in uncorrected_word:
    count_iteration += 1
    if count_iteration % 2 == 1:
        left_part += symbol
    else:
        right_part = symbol + right_part
print("Расшифрованное сообщение:", left_part + right_part)
