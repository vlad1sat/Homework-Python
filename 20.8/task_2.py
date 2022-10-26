def is_prime(number):
    count_det = 0
    for det in range(1, number + 1):
        if number % det == 0:
            count_det += 1
    return count_det == 2


def crypto(symbols):
    return [symbol for index, symbol in enumerate(symbols) if is_prime(index)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))