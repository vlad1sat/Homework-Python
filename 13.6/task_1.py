def create_number(number):
    whole_path = number
    factorial_path = 0
    while whole_path > 10 or whole_path <= 1:
        if number > 1:
            factorial_path += 1
            whole_path /= 10
        else:
            factorial_path -= 1
            whole_path *= 10
    print("Формат плавающей точки: x = ", round(whole_path, abs(factorial_path)), "* 10 **", factorial_path)


number = float(input("Введите число: "))
create_number(number)
