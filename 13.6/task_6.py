start_amplitude = float(input("Введите начальную амплитуду: "))
ended_amplitude = float(input("Введите амплитуду остановки: "))
count_amplitude = 0
while start_amplitude > ended_amplitude:
    start_amplitude -= (start_amplitude * 8.4 / 100)
    count_amplitude += 1
print("Маятник считается остановившимся через", count_amplitude, "колебаний")