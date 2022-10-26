def palindrome():
    is_odd = False
    checked_symbols = []
    for symbol in symbols:
        count_symbol = symbols.count(symbol)
        if symbol in checked_symbols:
            continue
        if count_symbol % 2 == 1:
            if is_odd:
                print("Нельзя сделать палиндромом!")
                return
            is_odd = True
        checked_symbols.append(symbol)
    print("Можно сделать палиндромом!")


user_str = input("Введите строку: ")
symbols = [symbol for symbol in user_str]
count_symbols = {}
palindrome()
