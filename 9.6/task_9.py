all_milk = 0
for stall in range(1, 11):
    command = input("Стойло свободно? a - свободное стойло, b - занятое. ")
    if command == 'b':
        all_milk += stall * 2
print("Молока произведено за день:", all_milk)
