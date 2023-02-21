import string

def draw_horizontal_line(width):
  return "-" * 4 * width

def get_new_line():
  return "\n"

def get_empty_board(width, height):
  board = list()
  cols = []
  for i in range(0, width):
    cols.append("#")
  for i in range(0, height):
    board.append(cols)
  return board