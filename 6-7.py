people = {
    'Den' : {
        'first' : 'Den',
        'last' : 'Shnaider',
        'city' : 'New',
    },
    'Alek' : {
        'first' : 'Alek',
        'last' : 'Gelts',
        'city' : 'Moskow',
    },
    'Mantr' : {
        'first' : 'Mantr',
        'last' : 'Shults',
        'city' : 'Piter',
    },
}

for peoplename, people_info in people.items():
    print("\nPeoplename: " + peoplename)
    full_name = people_info['first'] + " " + people_info['last']
    print("\tFullname: " + " " + full_name.title())
    print("\tCity: " + " " + people_info['city'].title())
