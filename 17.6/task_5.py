# немного модеренизирована
string = input("Введите строку: ")
start_symbol = -1
words = []
is_first = False

for index in range(len(string)):
    if string[index] == 'h':
        if not is_first:
            start_symbol = index + 1
            is_first = True
        else:
            words.append(string[start_symbol:index])
            start_symbol = index + 1

print("Последовательности между h, не включая пустоты:", [word[::-1] for word in words if word != ''])
