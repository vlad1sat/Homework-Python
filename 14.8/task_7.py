def correct_year(year):
    count_identical_symbol = 0
    result = []
    for number in range(0, 10):
        for symbol in str(year):
            if symbol == str(number):
                count_identical_symbol += 1
        if count_identical_symbol == 3:
            return result
        count_identical_symbol = 0


start_year = int(input("Введите первый год: "))
ended_year = int(input("Введите второй год: "))
print(f"Годы от {start_year} до {ended_year} с тремя одинаковыми цифрами:")
for year in range(start_year, ended_year + 1):
    if correct_year(year) is not None:
        print(year)
