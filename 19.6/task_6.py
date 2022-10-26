def word_in_dict(dictionary):
    word = input("Введите слово: ").lower()
    if word in dictionary.keys():
        print(f"Синоним: {dictionary[word].title()}")
    else:
        print("Такого слова в словаре нет.")


count_pairs = int(input("Введите количество пар слов: "))
dictionary_pair = {}

for index_pait in range(1, count_pairs + 1):
    pair = input(f"{index_pait}-я пара: ").lower().split(' — ')
    dictionary_pair[pair[0]] = pair[1]
    dictionary_pair[pair[1]] = pair[0]

count_words = int(input("Количество проверяемых слов: "))
for _ in range(count_words):
    word_in_dict(dictionary_pair)
