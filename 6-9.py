favplace = {
    'river' : ['Mika','Lika'],
    'city' : ['Kate'],
    'Sea' : ['Petr'],
}

for place, names in favplace.items():
    print("\n" + place.title() + " is a favourite place for:")
    for name in names:
        print("\t" + name.title())