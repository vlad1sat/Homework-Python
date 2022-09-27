lower_line = int(input("Нижняя граница: "))
upper_line = int(input("Верхняя граница: "))
step = int(input("Шаг: "))
last_temperature = 0
print("C\t   F")
for temperature in range(lower_line, upper_line, step):
    fahrenheit = 32 + temperature * 1.8
    last_temperature = temperature
    print(temperature, "\t", round(fahrenheit, 1))
if last_temperature < upper_line:
    print(upper_line, "\t", round(32 + upper_line * 1.8, 1))
