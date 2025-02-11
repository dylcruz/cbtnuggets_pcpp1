class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_details(self):
        print(f'{self.name} - {self.email} - {self.get_user_type()}')
    
    def get_user_type(self):
        return 'Basic User'
    
    def can_edit(self):
        return False
    
    def can_view(self):
        return True
    
    def can_delete(self):
        return False
    
    def can_delete_users(self):
        return False
    
    def can_reset_password(self):
        return False
    
class Editor(User):
    def get_user_type(self):
        return 'Editor'
    
    def can_edit(self):
        return True
    
class Admin(User):
    def get_user_type(self):
        return 'Admin'
    
    def can_edit(self):
        return True
    
    def can_delete(self):
        return True
    
    def brag_about_admin_privileges(self):
        print('I can do anything!')

class SuperAdmin(Admin):
    def get_user_type(self):
        return 'Super Admin'
    
    def can_delete_users(self):
        return True
    
    def can_reset_password(self):
        return True

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_species(self):
        return 'This animal does not have a defined species'

    def print_details(self):
        print(f'{self.name} is a {self.get_species()} and is {self.age} years old')

class Cat(Animal):
    def get_species(self):
        return 'Felis catus'
    
class Dog(Animal):
    def get_species(self):
        return 'Canis lupus familiaris'
    
class Elephant(Animal):
    def get_species(self):
        return 'Loxodonta africana'
    
u1 = User('u', 'u@email.com')
e1 = Editor('e', 'e@email.com')
a1 = Admin('a', 'a@email.com')
sa1 = SuperAdmin('sa', 'sa@email.com')

if sa1.can_delete_users():
    print('Y')
else:
    print('N')

users = [
    u1,
    e1,
    a1,
    sa1
]

cat = Cat('Nabi', 4)
dog = Dog('Buddy', 7)
elephant = Elephant('Dumbo', 12)

users_and_animals = [*users, cat, dog, elephant]

def print_user_data(user: User):
    print(f'{user.name} is a {user.get_user_type()}. Can edit: {user.can_edit()}. Can delete: {user.can_delete()}. Can delete users: {user.can_delete_users()}.')

for user in users:
    print_user_data(user)

def ask_what_they_do_for_a_living(admin: Admin):
    admin.brag_about_admin_privileges()

ask_what_they_do_for_a_living(sa1)

for x in users_and_animals:
    x.print_details()