class Restaurant:
    def __init__(self, restaurant_name, c_type):
        self.restaurant_name = restaurant_name
        self.type = c_type

    def describe_restaurant(self):
        print("\nИмя Ресторана: " + self.restaurant_name.title() + "." )
        print("\nТип Ресторана: " + self.type.title() + "." )
        
    def open_restaurant(self):
        print("\nРесторан " + self.restaurant_name.title() + " открыт!")   

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, c_type, flavors):
        super().__init__(restaurant_name, c_type)
        self.flavors = flavors

    def menu(self):
        for flavor in self.flavors:
            print(flavor)

my_restaurant = IceCreamStand('Polasko', 'Asian', ['Шоколадное', 'Ванильное', 'Клубничное'])
my_restaurant.menu()

