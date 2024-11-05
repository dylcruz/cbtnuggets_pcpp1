class Person:
    def __init__(self, name, age, hair_color, eye_color):
        print("Creating a new instance of the Person class.")
        self.name = name
        self. age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def greet(self, other_name):
        print(f'Hello {other_name}, my name is {self.name}!')

class Developer(Person):
    pass

class PythonDeveloper(Developer):
    pass

print(f'Developer is a subclass of Person: {issubclass(Developer, Person)}')
print(f'Person is a subclass of Developer: {issubclass(Person, Developer)}')
print(f'Python Developer is a subclass of Person: {issubclass(PythonDeveloper, Person)}')

person_1 = Developer("Dylan", 29, "black", "brown")
person_2 = Person("Haley", 29, "black", "brown")

person_1.greet('Haley')
person_2.greet('Dylan')

def print_person_details(person):
    if isinstance(person, Person):
        print(f'name: {person.name}, age: {person.age}')
    else:
        print('Not a person.')

person_3 = 0

print_person_details(person_1)
print_person_details(person_3)
