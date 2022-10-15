count_skates = int(input("Кол-во коньков: "))
skates = []
feet = []

for index in range(count_skates):
    skates.append(int(input(f"Размер {index + 1}-й пары: ")))

count_feet = int(input("\nКол-во людей: "))
for index in range(count_feet):
    feet.append(int(input(f"Размер ноги {index + 1}-го человека:  ")))

sorted(feet)
sorted(skates)
result = 0
count_result = 0
length_skates = len(skates)
for foot in feet:
    for skate in range(len(skates)):
        if foot <= skates[skate]:
            result += 1
            skates.remove(skates[skate])
            break

print("Наибольшее кол-во людей, которые могут взять ролики:" + result)

