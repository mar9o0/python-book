class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print("\nИнформация о пользователе: " + self.first_name.title() + ", " + self.last_name.title() + ", " + self.gender + ", " + self.age + ".")

    def greet_user(self):
        print("Добро пожаловать " + self.first_name.title() + " " + self.last_name.title() + "!")

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, privileges):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = privileges
    
    def priv(self):
        for privelege in self.privileges:
            print(privelege)

privet = Admin('Кристина', 'Петрова', 'женщина', '21 год', ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])
privet.priv()