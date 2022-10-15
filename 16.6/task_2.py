def get_class(class_people, start_height, end_height, step):
    for height in range(start_height, end_height + 1, step):
        class_people.append(height)


first_class = []
second_class = []
get_class(first_class, 160, 176, 2)
get_class(second_class, 162, 180, 3)
first_class.extend(second_class)
print(f"Отсортированный список учеников: {sorted(first_class)}")
