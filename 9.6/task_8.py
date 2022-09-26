length_header = int(input("Общую длину колонтитула: "))
screamers = int(input("Желаемое количество восклицательных знаков: "))
middle = (length_header - screamers) // 2
if middle == 0:
    print('~' * middle + '!' * screamers + '~' * middle)
else:
    print('~' * middle + '!' * screamers + '~' * (middle + 1))