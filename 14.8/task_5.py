# Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1.
def min_determinant(number):
    for determinant in range(2, number + 1):
        if number % determinant == 0:
            return determinant


number = int(input("Введите число: "))
print("Наименьший делитель, отличный от единицы:", min_determinant(number))
