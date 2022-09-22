cards = []
count_cards = int(input("Введите количество карточек: "))
for element_cards in range(1, count_cards + 1):
    cards.append(element_cards)
for card in range(len(cards) - 1):
    cards.remove(int(input("Введите номер оставшейся карточки: ")))
if len(cards) == 1:
    print("Номер пропавшей карточки:", cards[0])
else:
    print("Какие-то карточки неккоректно были введены!")
