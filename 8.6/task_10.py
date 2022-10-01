count_boys = int(input("Введите количество мальчиков: "))
count_girls = int(input("Введите количество девочек: "))
result = ""
if (count_boys > 2 * count_girls) or (count_girls > 2 * count_boys):
    print("Нет решения.")
elif count_boys >= count_girls:
    difference = count_boys - count_girls
    for bgb in range(difference):
        result += "BGB"
    for bg in range(count_girls - difference):
        result += "BG"
else:
    difference = count_girls - count_boys
    for gbg in range(difference):
        result += "GBG"
    for gb in range(count_boys - difference):
        result += "GB"
print(result)
