def get_city_country(countries, city):
    for country, cities in countries.items():
        if city in cities:
            print(f"Город {city} расположен в стране {country}.")
            return
    print(f"По городу {city} данных нет.")


count_country = int(input("Количество стран: "))
countries = {}

for index_country in range(1, count_country + 1):
    information = input(f"{index_country}-я страна: ").split()
    country = information[0]
    cities = {information[index_city] for index_city in range(1, len(information))}
    countries[country] = cities


first_city = input("Первый город: ")
get_city_country(countries, first_city)

second_city = input("Второй город: ")
get_city_country(countries, second_city)

third_city = input("Третий город: ")
get_city_country(countries, third_city)

