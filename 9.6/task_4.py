count_ranks = int(input("Введите количество рядов: "))
count_sits = int(input("Введите количество сидений: "))
count_pass = int(input("Введите количество метров между рядами: "))
for rank in range(count_ranks):
    print("=" * count_sits, "*" * count_pass, "=" * count_sits)
