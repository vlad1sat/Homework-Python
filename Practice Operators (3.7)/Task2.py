sums_quarters = []
for index in range(1, 5):
    sums_quarters.append(int(input("Введите сумму дохода квартала: ")))
print((sums_quarters[0] + sums_quarters[1]) / (sums_quarters[2] + sums_quarters[3]))
