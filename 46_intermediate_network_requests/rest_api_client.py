
import requests
import json

while True:
    print('\n- Web Store -')
    print('1. Get Product Info')
    print('2. Delete Product')
    print('3. Add Product')
    print('4. Update Product')
    menu_selection = int(input('\nEnter your selection: '))

    if menu_selection == 1:
        while True:
            all_products_json = requests.get('http://localhost:8000/products').json()

            print(f'\n- All Products -')
            for x in range(0, len(all_products_json)):
                print(f'{x + 1}. ' + all_products_json[x]['name'])
            print(f'{len(all_products_json) + 1}. Return')

            menu_selection = int(input('\nSelect a product to get more information: '))
            if menu_selection == (len(all_products_json) + 1):
                break

            elif menu_selection <= len(all_products_json):
                get_url = 'http://localhost:8000/products/' + all_products_json[menu_selection-1]['name']
                product_json = requests.get(get_url).json()
                print(f'\nProduct Name: {product_json["name"]}')
                print(f'Stock: {product_json["stock"]}')
                print(f'Price: {product_json["price"]}')

            else:
                print('Invalid input!')

    elif menu_selection == 2:
        while True:
            all_products_json = requests.get('http://localhost:8000/products').json()

            print(f'\n- All Products -')
            for x in range(0, len(all_products_json)):
                print(f'{x + 1}. ' + all_products_json[x]['name'])
            print(f'{len(all_products_json) + 1}. Return')

            menu_selection = int(input('\nSelect a product to delete: '))
            if menu_selection == (len(all_products_json) + 1):
                break

            elif menu_selection <= len(all_products_json):
                product_url = 'http://localhost:8000/products/' + all_products_json[menu_selection-1]['name']
                requests.delete(product_url)

    elif menu_selection == 3:
        new_product_name = input('\nEnter the products name: ')
        new_product_stock = int(input('Enter the stock of the product: '))
        new_product_price = int(input('Enter the price of the product: $'))

        request_data = {
            'name': new_product_name,
            'stock': new_product_stock,
            'price': new_product_price,
        }

        response = requests.post('http://localhost:8000/products/',
                                 data=json.dumps(request_data),
                                 headers={'Content-Type': 'application/json'})

        print('\nProduct created successfully')

    elif menu_selection == 4:
        while True:
            all_products_json = requests.get('http://localhost:8000/products').json()

            print(f'\n- All Products -')
            for x in range(0, len(all_products_json)):
                print(f'{x + 1}. ' + all_products_json[x]['name'])
            print(f'{len(all_products_json) + 1}. Return')

            menu_selection = int(input('\nSelect a product to update: '))
            if menu_selection == (len(all_products_json) + 1):
                break

            elif menu_selection <= len(all_products_json):
                product = all_products_json[menu_selection-1]
                print(f'\nUpdating {product["name"]}. Choose a field to update:')
                menu_selection = int(input('1. Name | 2. Stock | 3. Price | 4. Custom | : '))

                if menu_selection == 1:
                    product_new_name = input('Enter a new name for the product: ')
                    request_data = {'new_value': product_new_name, 
                                    'name': product['name'], 
                                    'update_value': 'name'}

                elif menu_selection == 2:
                    product_new_stock = int(input('Enter a new stock for the product: '))
                    request_data = {'new_value': product_new_stock, 
                                    'name': product['name'], 
                                    'update_value': 'stock'}

                elif menu_selection == 3:
                    product_new_price = int(input('Enter a new price for the product: '))
                    request_data = {'new_value': product_new_price, 
                                    'name': product['name'], 
                                    'update_value': 'price'}

                elif menu_selection == 4:
                    product_new_variable = input('Enter a new variable for the product: ')
                    new_variable_value = input('Enter a value for the new variable: ')
                    request_data = {'new_value': new_variable_value, 
                                    'name': product['name'], 
                                    'update_value': product_new_variable}
                    
                else:
                    print('Invalid Input!')
                    continue
                
                response = requests.put('http://localhost:8000/products/' + request_data['name'],
                                            data=json.dumps(request_data),
                                            headers={'Content-Type': 'application/json'})
                print('\nProduct updated successfully')
                    
    else:
        print('Invalid input!')
