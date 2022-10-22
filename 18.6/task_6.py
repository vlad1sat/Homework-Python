string_user = input("Введите строку: ")
result = ''
correct_symbol = string_user[:1]
count_symbols = 1

for index in range(1, len(string_user)):
    if string_user[index] == correct_symbol:
        count_symbols += 1
    else:
        result += ''.join([correct_symbol, str(count_symbols)])
        correct_symbol = string_user[index]
        count_symbols = 1

result += ''.join([correct_symbol, str(count_symbols)])
print(result)
