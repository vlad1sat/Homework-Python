end_collection = int(input("Введите число: "))
collection = []
for number in range(1, end_collection, 2):
    collection.append(number)
if end_collection % 2 == 1:
    collection.append(end_collection)
print(collection)