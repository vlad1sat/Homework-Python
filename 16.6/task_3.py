shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
tool_goal = input("Название детали: ").lower()
total_count_tools = int(input("Кол-во деталей — "))
count_tools = 0
total_sum = 0
for tool in shop:
    if count_tools == total_count_tools:
        break
    if tool[0] == tool_goal:
        total_sum += tool[1]
        count_tools += 1
if count_tools != total_count_tools:
    print(f"Деталей всего в магазине — {count_tools}")
print(f"Общая стоимость — {total_sum}")
