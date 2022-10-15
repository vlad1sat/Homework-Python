guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    command = input("Гость пришёл или ушёл? ").lower()
    if command == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if command == "пришел":
        if len(guests) >= 6:
            print(f"Прости, {name}, но мест нет.")
        else:
            guests.append(name)
            print(f"Привет, {name}!")
    elif command == "ушел":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print("Такого гостя нет!")
    else:
        print("Некорректная команда!")