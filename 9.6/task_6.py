text = input("Введите строку: ")
count_s = 0
max_s = 0
for symbol in range(len(text) - 1):
    if text[symbol] == 's':
        count_s += 1
        if count_s > max_s:
            max_s = count_s
    else:
        count_s = 0
print("Самая длинная последовательность:", max_s)
