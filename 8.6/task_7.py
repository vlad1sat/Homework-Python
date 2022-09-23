educational_grant = int(input('Введите размер степендии: '))
expenses = int(input('Введите расходы на проживание: '))
sums = expenses
for i in range(2, 11):
    expenses = expenses * 1.03
    sums = sums + expenses
print('У родителей необходимо попросить: ', round((sums - educational_grant * 10), 3) , 'рублей')
