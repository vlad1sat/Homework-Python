def append_in_list(list_elements, start, end):
    result = []
    for index in range(start, end):
        result.append(list_elements[index])
    return result


shift = int(input("Сдвиг: "))
# реализован ввод данных, а не изменение массива только через программу
list_elements = input("Введите числа через пробел: ").split()
list_elements = [int(item) for item in list_elements]
length = len(list_elements)
result = append_in_list(list_elements, length - shift, length) \
         + append_in_list(list_elements, 0, length - shift)
print("Сдвинутый список:", result)
