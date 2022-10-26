max_number = int(input("Введите максимальное число: "))
numbers = set(number for number in range(1, max_number + 1))

while True:
    user_numbers_str = input("Нужное число есть среди вот этих чисел: ")
    if user_numbers_str == "помогите!":
        print("Артём мог загадать следующие числа:", numbers)
        break
    user_numbers = set(int(number) for number in user_numbers_str.split())
    user_command = input("Ответ Артёма: ").lower()
    if user_command == "да":
        numbers &= user_numbers
    elif user_command == "нет":
        numbers -= user_numbers
    else:
        print("Неккоректная команда!")
