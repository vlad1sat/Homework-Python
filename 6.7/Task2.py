name = input("Введите ваше имя: ")
duty = int(input("Введите сумму долга: "))
print(name + ",", "ваша задолженность составляет", str(duty), "рублей.")
while True:
    contribution = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    if contribution < duty:
        print("Маловато,", name + ".", "Давайте ещё раз.")
    else:
        print("Отлично,", name + "!", "Вы погасили долг. Спасибо!")
        break
