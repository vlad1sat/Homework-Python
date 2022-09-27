import math

radius_planet = float(input("Введите радиус случайной планеты: "))
volume_planet = (4 / 3) * math.pi * radius_planet ** 3
volume_earth = 10.8321 * 10 ** 11
if volume_planet > volume_earth:
    print("Объём планеты Земля меньше в (1/" + str(round(volume_earth / volume_planet, 3)) + ")",
          round(volume_planet / volume_earth, 3), "= раз")
elif volume_planet < volume_earth:
    print("Объём планеты Земля больше в", round(volume_earth / volume_planet, 3), "раз")
else:
    print("Планеты по объему равны!")
