class Matrix:
    def __init__(self, *rows):
        self._matrix = [*rows]
    
    def __getitem__(self, value):
        if isinstance(value, int):
            return self._matrix[value]
        elif isinstance(value, tuple):
            if value[0] is None:
                column_list = []
                for x in range(len(self._matrix)):
                    column_list.append(self._matrix[x][value[1]])
                return column_list
            else:
                return self._matrix[value[0]][value[1]]
        
m1 = Matrix(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(m1[1])
print(m1[2, 2])
print(m1[None, 2])
