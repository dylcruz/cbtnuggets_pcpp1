import sqlite3

# 1. Add / Edit / Delete / List products
#   a. Add / Edit (name, price)
#   b. Delete (id)
# 2. Exit

def edit_database_menu():
    while True:
        print('\nEdit Database Menu')
        print('1. Add product')
        print('2. Edit product')
        print('3. Delete product')
        print('4. List products')
        print('5. Exit to main menu')
        user_input = int(input('Choose an option: '))
        if user_input == 1:
            add_product()
        elif user_input == 2:
            edit_product()
        elif user_input == 3:
            delete_product()
        elif user_input == 4:
            list_products()
        elif user_input == 5:
            return
        else:
            print('Invalid input')

def add_product():
    product_name = input('Enter the product name: ')
    product_price = int(input('Enter the product price: '))
    cursor.execute('''
    INSERT INTO products (name, price) VALUES (?, ?)
    ''', (product_name, product_price))
    connection.commit()
    print(f'{product_name} added successfully with price {product_price}.')

def edit_product():
    print('\nListing current products in the database...')
    list_products()
    id_choice = int(input('Enter the ID of the product you would like to update: '))
    new_name = input('Enter the new name for the product: ')
    new_price = input('Enter the new price of the product: ')
    cursor.execute('''
    UPDATE products SET name = ?, price = ? WHERE id = ?
    ''', (new_name, new_price, id_choice))
    connection.commit()
    print('Product updated successfully.')

def delete_product():
    print('\nListing current products in the database...')
    list_products()
    id_choice = int(input('Enter the ID of the product you would like to delete: '))
    cursor.execute('''
    DELETE FROM products WHERE id = ?
    ''', (id_choice,))
    connection.commit()
    print(f'Product with id {id_choice} successfully deleted from the database.')

def list_products():
    cursor.execute('''
    SELECT * from products
    ''')
    for product in cursor:
        print(product)

connection = sqlite3.connect('product-database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
    );''')
connection.commit()

while True:
    print('\n - Product Database -')
    print('1. Edit Database')
    print('2. Exit')
    user_input = int(input('Choose an option: '))
    if user_input == 1:
        edit_database_menu()
    if user_input == 2:
        break
    else:
        print('Invalid choice.')

print('Exiting program, closing DB connection.')
connection.close()