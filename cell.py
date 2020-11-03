class Cell:
  def __init__(self):
   ''' 
   holds cell's init status
   '''
   self._status = 'Dead'

  def set_dead(self):
   ''' 
   sets cell status to dead 
   '''
   self._status = 'Dead'
  
  def set_alive(self):
   '''
   sets cell status to alive
   '''
   self._status = 'Alive'
  
  def is_alive(self):
    '''
    checks if cell is alive
    returns True if alive, False if not
    '''
    if self._status == 'Alive':
      return True
    return False

  def get_print_character(self):
    '''
    method returning a status character of our choice to print on the board
    '''
    if self.is_alive():
      return 'O'
    return '.'