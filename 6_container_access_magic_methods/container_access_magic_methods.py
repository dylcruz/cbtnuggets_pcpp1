import datetime

class MyContainer:
    def __init__(self, name, date_created):
        self.name = name
        self.date_created = date_created
        self.values = []
    
    def add_value(self, value):
        self.values.append(value)
    
    def __getitem__(self, index):
        if isinstance(index, str):
            return object.__getattribute__(self, index)
        elif isinstance(index, int):
            return self.values[index]
        elif isinstance(index, slice):
            values = self.values[index]
            new_container = MyContainer('My Slice', datetime.datetime.now())
            for x in values:
                new_container.add_value(x)
            return new_container
        elif isinstance(index, tuple):
            values_list = []
            for x in index:
                values_list.append(self[x])
            return values_list
        else:
            return NotImplemented
    
    def __setitem__(self, index, value):
        self.values

    def __delitem__(self, index):
        del self.values[index]

c1 = MyContainer('My First Container', datetime.datetime.now())

c1.add_value(0)
c1.add_value(1)
c1.add_value(2)
c1.add_value(3)
c1.add_value(4)

print(c1[1:3]['name'])
print(c1[1:3][0])
print(c1[1, 2, 'name'])
