count_students = int(input("Введите количество учеников: "))
count_marks = [0, 0, 0]
for student in range(count_students):
    mark = int(input("Введите оценку за тест: "))
    if mark == 3:
        count_marks[0] += 1
    elif mark == 4:
        count_marks[1] += 1
    else:
        count_marks[2] += 1
message = "Больше всего в классе"
if max(count_marks) == count_marks[0]:
    print(message, "троечников")
elif max(count_marks) == count_marks[1]:
    print(message, "хорошистов")
else:
    print(message, "отличников")
