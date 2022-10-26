score_table = {}
count_protocols = int(input("Общее количество строк протокола: "))
print("Записи (результат и имя):")
for time in range(count_protocols):
    result, name = input(f"{time + 1} запись: ").split()
    result = int(result)
    if name in score_table:
        if result > score_table[name][0]:
            score_table[name][0] = result
            score_table[name][1] = time
    else:
        score_table[name] = [result, time]

scores = list(score_table.items())
scores.sort(key=scores[1][0] - scores[1][1], reverse=True)
print("\nИтоги соревнований:")
for winner_index in range(2):
    print(f"{winner_index + 1} место. {scores[winner_index][0]} {scores[winner_index][1][0]}")


