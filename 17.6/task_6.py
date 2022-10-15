message = input("Введите числа через пробел: ").split()

list_without_filter = [int(symbol) for symbol in message]
print("Список до сжатия:", list_without_filter)
print("Список после сжатия:", [number for number in list_without_filter if number > 0])
