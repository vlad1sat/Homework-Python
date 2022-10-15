def palindrome(elements_word):
    first_part = ""
    last_part = ""
    for index in range(len(elements_word)):
        if index < len(elements_word) // 2:
            first_part += elements_word[index]
        else:
            last_part += elements_word[index]
    return first_part == last_part[::-1]


word = list(input("Введите слово: "))
if len(word) % 2 == 1:
    word.pop(len(word) // 2)
if palindrome(word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
