import json
import os
db_file = 'json_db.json'
db_found = os.path.exists(db_file)

print('JSON Database Update Program')

if db_found:
    with open(db_file, 'r') as file:
        db_data = json.load(file)
    print('Existing DB found! Printing current values: ')
    for key, value in db_data.items():
        print(f'{key}: {value}')

print('\nEnter a value to update the database, or press enter to skip.')
name = input('Name: ')
try:
    age = int(input('Age: '))
except ValueError:
    age = 0
favorite_foods = []
while True:
    food = input('Please enter your favorite foods one at a time. Enter to end: ')
    if len(food) == 0:
        break
    else:
        favorite_foods.append(food)

db_entry = {}

if len(name) == 0 and db_found:
    db_entry['name'] = db_data['name']
else:
    db_entry['name'] = name

if len(age) == 0 and db_found:
    db_entry['age'] = db_data['age']
else:
    db_entry['age'] = age

if len(favorite_foods) == 0 and db_found:
    db_entry['favorite_foods'] = db_data['favorite_foods']
else:
    db_entry['favorite_foods'] = favorite_foods

with open('json_db.json', 'w') as file:
    json.dump(db_entry, file)

print('DB updated successfully. Goodbye.')
quit()
