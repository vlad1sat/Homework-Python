goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for good, id_good in goods.items():
    elements_by_id = store.get(id_good)
    price_goods = 0
    count_goods = 0
    for element in elements_by_id:
        count_goods += element.get('quantity')
        price_goods += element.get('quantity') * element.get('price')
    print(f"{good} — {count_goods} штук, стоимость {price_goods} рублей")