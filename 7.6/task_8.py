for number in range(10, 100):
    sum_number = 1
    for symbol in str(number):
        sum_number *= int(symbol)
    if sum_number * 3 == number:
        print(number)
