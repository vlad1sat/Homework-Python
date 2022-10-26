array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([(array[index_number], array[index_number + 1]) for index_number in range(0, len(array), 2)])
