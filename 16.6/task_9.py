count_friends = int(input("Кол-во друзей: "))
papers = int(input("Долговых расписок: "))
balance = []

for _ in range(0, count_friends):
    balance.append(0)
for paper in range(1, papers + 1):
    print(f"\n{paper}-я расписка")
    add_balance = int(input("Кому: ")) - 1
    minus_balance = int(input("От кого: ")) - 1
    sum_operation = int(input("Сколько: "))
    balance[add_balance] += sum_operation
    balance[minus_balance] -= sum_operation

print("\nБаланс друзей:")
for index in range(1, len(balance) + 1):
    print(f"{index}: {balance[index - 1]}")
