class Restaurant:
    def __init__(self, restaurant_name, c_type):
        self.restaurant_name = restaurant_name
        self.type = c_type

    def describe_restaurant(self):
        print("\nИмя Ресторана: " + self.restaurant_name.title() + "." )
        print("\nТип Ресторана: " + self.type.title() + "." )
        
    def open_restaurant(self):
        print("\nРесторан " + self.restaurant_name.title() + " открыт!")   

my_restaurant = Restaurant('Polasko', 'Asian')
    
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()