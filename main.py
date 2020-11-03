from board import Board

def main():
  # get the grid size:
  user_rows = int(input('Input no. of rows: '))
  user_cols = int(input('Input no. of columns: '))

  # create a board: 
  game_of_life_board = Board(user_rows, user_cols)

  game_of_life_board.draw_board()

  user_action = ''
  while user_action != 'x':
    user_action = input('Press Enter to add a generation or X to quit: ')

    if user_action == '':
      game_of_life_board.update_board()
      game_of_life_board.draw_board()

main()
