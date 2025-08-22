class Restaurant:
    def __init__(self, restaurant_name, c_type):
        self.restaurant_name = restaurant_name
        self.type = c_type
        self.number_served = 0

    def restaurant(self):
        print("Забарнировано столиков на данный момент: " + str(self.number_served))

    def set_number_served(self, guests):
        self.guests = guests
        print("Обслужено гостей на данный момент: " + self.guests) 

    def increment_number_served(self, posit):
        self.number_served += posit


    def describe_restaurant(self):
        print("\nИмя Ресторана: " + self.restaurant_name.title() + "." )
        print("\nТип Ресторана: " + self.type.title() + "." )
        
    def open_restaurant(self):
        print("\nРесторан " + self.restaurant_name.title() + " открыт!")   

my_restaurant = Restaurant('Polasko', 'Asian')
    
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 23
my_restaurant.restaurant()
my_restaurant.increment_number_served(20)
