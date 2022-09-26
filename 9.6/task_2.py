count_correct_words = 0
for index in range(10):
    message = input("Введите кодовое слово: ").lower()
    if message == "карамба":
        count_correct_words += 1
print("Количество верных слов:", count_correct_words)
