all_seconds = int(input("Введите количество секунд: "))
for seconds in range(all_seconds, 0, -1):
    print("Количество секунд: ", seconds)
    analyzer = int(input("Вы готовы забрать еду? "))
    if analyzer == 1:
        print("Ваша еда готова, можно забрать. Таймер остановился на", seconds, "секунде.")
        exit()
print("Ваша еда готова, осторожно, горячо!")
