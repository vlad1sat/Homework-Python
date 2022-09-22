number = int(input("Введите число: "))
number = str(abs(number))
if len(number) == 2:
    print("Число двузначное.")
else:
    print("Число не двузначное.")
