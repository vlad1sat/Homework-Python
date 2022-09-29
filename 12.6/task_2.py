def test():
    number = int(input("Введите число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Некорректный ввод")
        test()


def positive():
    print("Положительное!")


def negative():
    print("Отрицательное!")


test()
