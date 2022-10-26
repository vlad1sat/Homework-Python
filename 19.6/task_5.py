text = input("Введите текст: ")
pairs = {}

symbols = [symbol for symbol in text]
for special_symbol in symbols:
    count_special_symbol = symbols.count(special_symbol)
    if pairs.get(count_special_symbol):
        if special_symbol in pairs.get(count_special_symbol):
            continue
        else:
            pairs[count_special_symbol].append(special_symbol)
    else:
        pairs[count_special_symbol] = [special_symbol]

for key, value in pairs.items():
    print(f"{key}: {value}")
