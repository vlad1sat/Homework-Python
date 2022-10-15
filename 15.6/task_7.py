count_boxes = int(input("Количество контейнеров: "))
boxes = []
index_box = 0
while index_box < count_boxes:
    box = int(input("Введите вес контейнера: "))
    if box > 200 or box < 1:
        print("Неверное значение!")
        continue
    boxes.append(box)
    index_box += 1
special_box = int(input("Введите вес нового контейнера: "))
result = -1
for index in range(0, count_boxes):
    if boxes[index] < special_box:
        result = index
        break
print("Номер, который получит новый контейнер:", result + 1)