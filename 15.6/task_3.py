length_line = int(input("Количество клеток: "))
result = []
for index in range(1, length_line + 1):
    efficiency = int(input(f"Эффективность {index} клетки: "))
    if efficiency < index:
        result.append(efficiency)
print("Неподходящие значения: ", result)
