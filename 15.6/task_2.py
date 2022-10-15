names = input("Введите имени через запятую: ").split(', ')
result = []
for index in range(0, len(names), 2):
    result.append(names[index])
print(result)
