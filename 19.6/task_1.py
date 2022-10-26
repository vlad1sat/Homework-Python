violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
result = 0

count_songs = int(input("Сколько песен выбрать? "))
for index_song in range(1, count_songs + 1):
    song = input(f"Название {index_song}-й песни:")
    if violator_songs.get(song):
        result += violator_songs.get(song)
    else:
        print("Такой песни нет в списке!")

print(f"Общее время звучания песен: {result} минут")