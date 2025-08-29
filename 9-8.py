class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privelege in self.privileges:
            print(privelege)

class Admin():
    def __init__(self, first_name, last_name, gender, age, privileges):
        self.privileges = privileges

admin = Privileges(['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])
admin.show_privileges()