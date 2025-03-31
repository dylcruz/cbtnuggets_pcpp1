from cell import Cell

class Spreadsheet:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = [[Cell(self) for _ in range(columns)] for _ in range(rows)]

    def get_cell(self, row, column):
        return self.cells[row][column]
    
    def __getitem__(self, name):
        pass

    def __setitem__(self, name, value):
        pass
