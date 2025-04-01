from cell import Cell

cell1 = Cell(None)
cell2 = Cell(None)

cell1.set_content('10')
cell2.set_content('20')

print(cell1 + cell2)
print(cell1 * cell2)
print(cell1 + 5)
print(5 * cell2)
