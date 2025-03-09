import sqlite3

connection = sqlite3.connect('my_first_database.db')
cursor = connection.cursor()

create_table_statement = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''

create_product_table_statement = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
)
'''

cursor.execute(create_table_statement)
connection.commit()

cursor.execute(create_product_table_statement)
connection.commit()

# insert_user_statement = '''
# INSERT INTO users (name, email) VALUES ('Bob Smith', 'bsmith@gmail.com')
# '''

# cursor.execute(insert_user_statement)
# connection.commit()

select_users_statement = '''
SELECT (email) FROM users
'''

cursor.execute(select_users_statement)

for user in cursor:
    print(user)

# user_dictionaries = []

# for user in cursor:
#     user_dictionaries.append({
#         'id': user[0],
#         'name': user[1],
#         'email': user[2]
#     })

# for user in user_dictionaries:
#     print(user)

create_product_statement = '''
INSERT INTO products (name, description, price) VALUES ('PS5', 'Sony PlayStation 5 Digital Edition', 49999)
'''
cursor.execute(create_product_statement)
connection.commit()


select_product_statement = '''
SELECT * FROM products
'''

cursor.execute(select_product_statement)

for product in cursor:
    print(product)

connection.close()
