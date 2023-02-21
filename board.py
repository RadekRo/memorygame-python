def get_empty_board(width, height):
  board = list()
  cols = []
  for i in range(0, width):
    cols.append("#")
  for i in range(0, height):
    board.append(cols)
  return board