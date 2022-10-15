import random


def create_random_collection():
    return [round(random.random() * 5 + 5, 2) for _ in range(20)]


first_team = create_random_collection()
second_team = create_random_collection()

print("Первая команда:", first_team)
print("Вторая команда:", second_team)
print("Победители тура:", [first_team[index] if first_team[index] >= second_team[index] else second_team[index]
                           for index in range(20)])
