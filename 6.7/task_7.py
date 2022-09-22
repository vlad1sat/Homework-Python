hour = 1
count_tasks = 0
call_wife = False
while hour < 9:
    print(str(hour) + "-й час")
    count_tasks += int(input("Сколько задач решит Максим? "))
    take_call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if take_call == 1:
        call_wife = True
    hour += 1
print("Рабочий день закончился. Всего выполнено задач:", count_tasks)
if call_wife:
    print("Нужно зайти в магазин.")
