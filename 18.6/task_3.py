uncorrected_symbols = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
path = input("Название файла: ")

for uncorrected_symbol in uncorrected_symbols:
    if path.startswith(uncorrected_symbol):
        print("Ошибка: название начинается на один из специальных символов.")
        exit()

if path.endswith('.txt') or path.endswith('.docx'):
    print("Файл назван верно.")
else:
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
