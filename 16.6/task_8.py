count_people = int(input("Кол-во человек: "))
people = []
number = int(input("Какое число в считалке? "))
end_count = 0
print(f"Значит, выбывает каждый {number}-й человек\n")
for num in range(1, count_people + 1):
    people.append(num)
while len(people) > 1:
    if end_count >= len(people):
        end_count = 0
    print(f"Текущий круг людей: {people}")
    print(f"Начало счёта с номера {people[end_count]}")
    index_bye = end_count
    while True:
        is_throw = False
        for person in range(end_count, len(people)):
            if index_bye == number - 1:
                print(f"Выбывает человек под номером {people[person]}\n")
                end_count = people.index(people[person])
                people.remove(people[person])
                is_throw = True
                break
            index_bye += 1
        if is_throw:
            break

print(f"\nОстался человек под номером {people[0]}")
