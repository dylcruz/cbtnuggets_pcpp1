import json

# Strings
# json.loads # JSON --> Python
# json.dumps # Python --> JSON

# # Files
# json.load # JSON --> Python
# json.dump # Python --> JSON

person = { 'name': 'Dylan', 'age': 29, 'hair': 'black' }
numbers = [1, 2, 3, 4, 5]

print(json.dumps(person))
print(json.dumps(numbers))

json_string = '{"a": 1, "b": 2, "c": 3}'

dictionary = json.loads(json_string)
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['c'])

with open('json_basics.json', 'r') as file:
    python_data = json.load(file)

print(python_data)

with open('json_basics.json', 'w') as file:
    json.dump(person, file)
