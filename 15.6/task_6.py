word = input("Введите слово: ")
corrected_symbols = []
uncorrected_symbols = []
for symbol in word:
    if symbol in uncorrected_symbols:
        continue
    if symbol not in corrected_symbols:
        corrected_symbols.append(symbol)
    else:
        corrected_symbols.remove(symbol)
        uncorrected_symbols.append(symbol)
print("Количество уникальных букв:", len(corrected_symbols))
