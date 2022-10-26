def add_contact():
    full_name = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").split())
    number = int(input("Введите номер телефона: "))
    if full_name in people:
        print("Такой человек уже есть в контактах.")
    else:
        people[full_name] = number
    print("Текущий словарь контактов:", people)


def find_person():
    surname = input("Введите фамилию для поиска: ")
    is_find = False
    for full_name, number in people.items():
        if surname in full_name:
            is_find = True
            print(f"({full_name[0]}, {full_name[1]}: {number})")
    if not is_find:
        print("Такого человека нет в контактах!")


people = dict()
while True:
    print("Введите номер действия:\n1. Добавить контакт\n2. Найти человека")
    command = int(input())
    if command == 1:
        add_contact()
    elif command == 2:
        find_person()
    else:
        print("Некорректная команда!")
        break
