import math

o_set = object.__setattr__
o_get = object.__getattribute__

in_conversions = {
    'in': 1,
    'cm': 2.45,
    'm': 0.0245,
    'ft': 0.083333333333333334,
}

age_conversions = {
    'years': 1,
    'months': 12,
    'days': 365,
    'hours': 365 * 24,
    'minutes': 365 * 24 * 60,
    'seconds': 365 * 24 * 60 * 60,
}

class Person:
    def __init__(self, first_name, last_name, age, height):
        o_set(self, 'first_name', first_name)
        o_set(self, 'last_name', last_name)
        o_set(self, 'age', age)
        o_set(self, 'height', height)

    def __getattribute__(self, name):
        if name == 'full_name':
            return o_get(self, 'first_name') + ' ' + o_get(self, 'last_name')
        elif name.startswith('age_'):
            units = name.split('_')[1]
            age = o_get(self, 'age')
            if units in age_conversions:
                return age * age_conversions[units]
            else:
                return NotImplemented
            
        elif name.startswith('height_'):
            units = name.split('_')[1]
            height = o_get(self, 'height')
            if units in in_conversions:
                return height * in_conversions[units]
            else:
                return NotImplemented
        
        return o_get(self, name)
    
    def __setattr__(self, name, value):
        if name == 'full_name':
            first_name, last_name = value.split(' ')
            o_set(self, 'first_name', first_name)
            o_set(self, 'last_name', last_name)

        elif name == 'age':
            print(f'Error! Age attribute is read-only! Age remains {o_get(self, "age")}')
        
        elif name.startswith('age_'):
            units = name.splt('_')[1]
            if units in age_conversions:
                o_set(self, 'age', value / age_conversions[units])
        
        elif name.startswith('height_'):
            units = name.split('_')[1]
            if units in in_conversions:
                o_set(self, 'height', value / in_conversions[units])
        
        o_set(self, name, value)

    def __delattr__(self, name):
        if name == 'age':
            print(f'Error! Age attribute is read-only! Age remains {o_get(self, "age")}')
            return
        object.__delattr__(self, name)

    def birthday(self):
        new_age = (self.age + 1)
        o_set(self, 'age', new_age)

