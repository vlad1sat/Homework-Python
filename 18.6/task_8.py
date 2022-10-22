first_str = input("Первая строка: ")
second_str = input("Вторая строка: ")

if first_str == second_str:
    print("Строки одинаковые.")
else:
    if len(first_str) != len(second_str):
        print('Строки разной длины.')
    else:
        shift = 1
        is_correct = False
        for index in range(len(first_str) - 1):
            second_str = second_str[-1] + second_str[:-1]
            if first_str == second_str:
                print(f"Первая строка получается из второй со сдвигом {shift}.")
                is_correct = True
                break
            else:
                shift += 1
        if not is_correct:
            print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
