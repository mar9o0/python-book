cities = {
    'Piter' : {
        'country' : 'Russia',
        'population' : '8Million',
        'fact' : 'beutiful',
    },

    'Moskva' : {
        'country' : 'Russia',
        'population' : '12Million',
        'fact' : 'beutiful',
    },

    'Rostov' : {
        'country' : 'Russia',
        'population' : '7Million',
        'fact' : 'beutiful',
    },

}

for city, city_info in cities.items():
    print("\nCity: " + city)
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("\tCountry: " + country.title())
    print("\tPopulation: " + population)
    print("\tFact: " + fact.title()) 