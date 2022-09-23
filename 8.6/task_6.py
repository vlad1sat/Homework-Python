size_letter = int(input("Введите размер письма: "))
count_folding = 0
for folding in range(12, size_letter, size_letter//2):
    count_folding += 2
print("Количество сворачиваний, чтобы поместить письмо в конверт 12x12:", count_folding)
