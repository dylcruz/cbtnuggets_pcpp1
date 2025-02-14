import requests

# response = requests.get('http://localhost:8000/products')
# print(response.json())

while True:
    print('\n- Web Store -')
    print('1. Get Product Info')
    print('2. Delete Products')
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
                print(f'\nProduct Name: {product_json['name']}')
                print(f'Stock: {product_json['stock']}')
                print(f'Price: {product_json['price']}')

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


    else:
        print('Invalid input!')
