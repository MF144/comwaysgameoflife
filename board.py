from cell import Cell
from random import randint

class Board:
  def __init__ (self, rows, cols):
    '''  
    Gets input from user to fill the grid with cells
    '''
    self._rows = rows
    self._cols = cols
    self._grid = [[Cell() for col_cells in range(self._cols)] for row_cells in range(self._rows)]

    self._generate_board()

  def draw_board(self):
    '''  
    Creates the board 
    '''
    print('\n'*10)
    print('Printing board')
    for row in self._grid:
      for col in row:
        print (col.get_print_character(), end='')
      print () # to create a new line and row
  
  def _generate_board(self):
    '''  
    Sets the random states for all cells
    '''
    for row in self._grid:
      for col in row:
        chance_number = randint(0, 2)
        if chance_number == 1:
         col.set_alive()

  def update_board(self):

    goes_alive = []
    gets_killed = []

    for row in range(len(self._grid)):
      for col in range(len(self._grid[row])):

        # check neighbor per square:
        check_neighbor = self.check_neighbor(row, col)

        living_neighbors_count = []
        
        for neighbor_cell in check_neighbor:
          #check live status for neighbor_cell:
          if neighbor_cell.is_alive():
            living_neighbors_count.append(neighbor_cell)

        cell_object = self._grid[row][col]
        status_main_cell = cell_object.is_alive()

        #If cell is alive, check neighbor status
        if status_main_cell == True:
          if len(living_neighbors_count) < 2 or len(living_neighbors_count) > 3:
            gets_killed.append(cell_object)  
          if len(living_neighbors_count) == 2 or len(living_neighbors_count) == 3:
            goes_alive.append(cell_object)
        else:
          if len(living_neighbors_count) == 3:
            goes_alive.append(cell_object)

      for cell_items in goes_alive:
          cell_items.set_alive()

      for cell_items in gets_killed:
          cell_items.set_dead()

  def check_neighbor(self, check_row, check_col):

    search_min = -1
    search_max = 2

    neighbor_list = []
    for row in range(search_min, search_max):
      for col in range(search_min, search_max):
        neighbor_row = check_row + row
        neighbor_col = check_col + col

        valid_neighbor = True

        if (neighbor_row) == check_row and (neighbor_col) == check_col:
          valid_neighbor = False

        if (neighbor_row) < 0 or (neighbor_row) >= self._rows:
          valid_neighbor = False

        if (neighbor_col) < 0 or (neighbor_col) >= self._cols:
          valid_neighbor = False

        if valid_neighbor:
          neighbor_list.append(self._grid[neighbor_row][neighbor_col])

    return neighbor_list