import math

text = input("Введите коэфиценты через пробел: ").split()
odds = [float(number) for number in text]
D = (odds[1] ** 2) - (4 * odds[0] * odds[2])
if D > 0:
    x1 = ((-odds[1]) + math.sqrt(D)) / (2 * odds[0])
    x2 = ((-odds[1]) - math.sqrt(D)) / (2 * odds[0])
    print("x1=", round(x1, 3), "x2=", round(x2, 3))
elif D == 0:
    print("x1=x2=", -(odds[1] / 2 * odds[0]))
