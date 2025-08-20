def city_country(city, country):
    full_adres = city + " - " + country
    return full_adres.title()

adres = city_country('Moskva', 'Russia')
print(adres)
