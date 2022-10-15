violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

total_count_songs = int(input("Сколько песен выбрать? "))
total_time = 0
for index in range(1, total_count_songs + 1):
    name_song = input(f"Название {index}-й песни: ")
    for song in violator_songs:
        if song[0] == name_song:
            total_time += song[1]
            break

print(f"\nОбщее время звучания песен: {round(total_time, 2)} минуты")
