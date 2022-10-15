count_cards = int(input("Количество видеокарт: "))
cards = []
for index in range(1, count_cards + 1):
    cards.append(int(input(f"{index} Видеокарта: ")))
print("Старый список видеокарт:", cards)
max_value = max(cards)
result = []
for card in cards:
    if card != max_value:
        result.append(card)
print("Новый список видеокарт:", result)
