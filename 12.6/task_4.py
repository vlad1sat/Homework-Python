def expand_number(number):
    result = ""
    for symbol in range(len(number) - 1, -1, -1):
        if number[symbol] == '0' and result == "":
            continue
        result += number[symbol]
    if result == "":
        print("Число состоит из 0!")
    else:
        print("Число наоборот:", result)


while True:
    accepted_values = input("Введите число: ")
    if accepted_values == '0':
        break
    expand_number(accepted_values)
