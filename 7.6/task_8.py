for number in range(10, 100):
    sum_number = 1
    for char in str(number):
        sum_number *= int(char)
    if sum_number * 3 == number:
        print(number)
