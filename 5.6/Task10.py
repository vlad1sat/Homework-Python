hour = int(input("Время прихода за посылкой: "))
if (10 <= hour < 12) or (hour == 14) or (18 <= hour < 20) or (hour >= 22) or (hour < 8):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")
