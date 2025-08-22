class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attem = 0

    def describe_user(self):
        print("\nИнформация о пользователе: " + self.first_name.title() + ", " + self.last_name.title() + ", " + self.gender + ", " + self.age + ".")

    def greet_user(self):
        print("Добро пожаловать " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attem(self):
        print("Количество попыток входа: " + str(self.login_attem))
        self.login_attem += 1

    def  reset_login_attem(self):
        self.login_attem = 0

 
user_1 = User('Кристина', 'Петрова', 'женщина', '21 год')

user_1.describe_user() 
user_1.greet_user() 

user_1.increment_login_attem()
user_1.increment_login_attem()
user_1.increment_login_attem()
user_1.increment_login_attem()

user_1.reset_login_attem()

print(user_1.increment_login_attem())