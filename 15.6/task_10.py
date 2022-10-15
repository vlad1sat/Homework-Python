# реализован ввод данных, а не изменение массива только через программу
list_elements = input("Введите числа через пробел: ").split()
list_elements = [int(item) for item in list_elements]   # используется для изменения строкового листа в лист чисел
print("Изначальный список:", list_elements)
print("Отсортированный список:", sorted(list_elements))
