import requests

class JokeSelector():
    def __init__(self):
        self.categories = {
            'Programming': False,
            'Miscellaneous': False,
            'Dark': False,
            'Pun': False,
            'Spooky': False,
            'Christmas': False,
        }

        self.blacklist_flags = {
            'nsfw': False,
            'religious': False,
            'political': False,
            'racist': False,
            'sexist': False,
            'explicit': False,
        }

        self.base_url = 'https://v2.jokeapi.dev/joke/'
        self.default_url = 'https://v2.jokeapi.dev/joke/Any' 

        self.verbose_mode = True

    def main_menu(self):
        while True:
            print('\n- Joke Generator Main Menu -\n')
            print('Please choose an option:')
            menu_selection = str(input('(C)ategories - (B)lacklists - (G)enerate Joke: '))

            if menu_selection[0].lower() == 'c':
                self.category_menu()
            elif menu_selection[0].lower() == 'b':
                self.blacklist_menu()
            elif menu_selection[0].lower() == 'g':
                self.get_joke()
            else:
                print('Invalid input!')

    def category_menu(self):
        print('- Joke Generator Category Menu -')
        while True:
            enabled_categories = [category for category in self.categories.keys() if self.categories[category] == True]
            disabled_categories = [category for category in self.categories.keys() if self.categories[category] == False]
            print(f'\nCurrently enabled categories: {enabled_categories}')
            print(f'Currently disabled categories: {disabled_categories}')
            
            menu_input = input('\nEnter a category to enable or disable it. Type "all" to enable all, or "none" to disable all. (Q) to return: ')
            if menu_input.lower() == 'all':
                self.set_all_categories()
            elif menu_input.lower() == 'none':
                self.unset_all_catergories()
            elif menu_input in self.categories.keys():
                if self.categories[menu_input] == False:
                    self.categories[menu_input] = True
                elif self.categories[menu_input] == True:
                    self.categories[menu_input] = False
            elif menu_input.lower() == 'q':
                return
            else:
                print('Invalid input.')

    def blacklist_menu(self):
        print('- Joke Generator Blacklist Menu -')
        while True:
            enabled_blacklist_flags = [category for category in self.blacklist_flags.keys() if self.blacklist_flags[category] == True]
            disabled_blacklist_flags = [category for category in self.blacklist_flags.keys() if self.blacklist_flags[category] == False]
            print(f'\nCurrently enabled blacklist flags: {enabled_blacklist_flags}')
            print(f'Currently disabled blacklist flags: {disabled_blacklist_flags}')
            
            menu_input = input('\nEnter a flag to enable or disable it. Type "all" to enable all, or "none" to disable all. (Q) to return: ')
            if menu_input.lower() == 'all':
                self.set_all_blacklist_flags()
            elif menu_input.lower() == 'none':
                self.unset_all_blacklist_flags()
            elif menu_input in self.blacklist_flags.keys():
                if self.blacklist_flags[menu_input] == False:
                    self.blacklist_flags[menu_input] = True
                elif self.blacklist_flags[menu_input] == True:
                    self.blacklist_flags[menu_input] = False
            elif menu_input.lower() == 'q':
                return
            else:
                print('Invalid input.')

    def get_joke(self):
        joke_raw = self.generate_request()
        joke_json = joke_raw.json()

        if self.verbose_mode:
            print(f'\nCategory: {joke_json["category"]} - Type: {joke_json["type"]} - '
                  + f'ID: {joke_json["id"]}')
            flags = [flag for flag in joke_json["flags"] if joke_json["flags"][flag] is True]
            print(f'Blacklist flags: {flags}')

        if joke_json['type'] == 'single':
            print('\n' + joke_json['joke'])
        elif joke_json['type'] == 'twopart':
            print('\n' + joke_json['setup'])
            print(joke_json['delivery'])

    def set_all_categories(self):
        for key in self.categories.keys():
            self.categories[key] = True

    def unset_all_catergories(self):
        for key in self.categories.keys():
            self.categories[key] = False

    def set_all_blacklist_flags(self):
        for key in self.blacklist_flags.keys():
            self.blacklist_flags[key] = True

    def unset_all_blacklist_flags(self):
        for key in self.blacklist_flags.keys():
            self.blacklist_flags[key] = False
    
    def generate_request(self):
        enabled_categories = [category for category in self.categories.keys() if self.categories[category] == True]
        enabled_blacklist_flags = [category for category in self.blacklist_flags.keys() if self.blacklist_flags[category] == True]

        categories_string = ','.join(enabled_categories)
        blacklist_flags_string = ','.join(enabled_blacklist_flags)

        if len(enabled_categories) == 0 and len(enabled_blacklist_flags) == 0:
            response = requests.get(self.default_url)
        elif len(enabled_categories) == 0:
            request_url = self.default_url + '?blacklistFlags=' + blacklist_flags_string
            response = requests.get(request_url)
        else:
            request_url = self.base_url + categories_string + '?blacklistFlags=' + blacklist_flags_string
            response = requests.get(request_url)

        return response
    
if __name__ == '__main__':
    js = JokeSelector()
    js.main_menu()