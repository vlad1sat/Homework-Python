size_file = float(input("Укажите размер файла для скачивания: "))
speed = float(input("Какова скорость вашего соединения? "))
downloaded = 0
timer = 0
while downloaded < size_file:
    timer += 1
    downloaded += speed
    percent = round(downloaded / size_file * 100)
    percent = 100 if percent > 100 else percent
    downloaded = size_file if downloaded > size_file else downloaded
    print("Прошло", timer, "сек. Скачано", downloaded, "из", size_file, "Мб",
          "(" + str(percent) + "%)")