count_offer = int(input("Введите количество заказов: "))
offers = {}


for index_offer in range(1, count_offer + 1):
    offer = input(f"{index_offer}-й заказ: ").split()
    if offers.get(offer[0]):
        if offer[1] in offers[offer[0]].keys():
            offers[offer[0]][offer[1]] += int(offer[2])
        else:
            offers[offer[0]][offer[1]] = int(offer[2])
    else:
        offers[offer[0]] = {offer[1]: int(offer[2])}


for name, name_offer in offers.items():
    print(name)
    sorted_name_offer = sorted(name_offer.items())
    for position, count_position in sorted_name_offer:
        print(f"\t{position}: {count_position}")
