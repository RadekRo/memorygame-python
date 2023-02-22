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

def display_board(board):
  board_width = len(board[0])
  current_row = 1
  draw_board = "   |"
  for i in range(0, board_width):
    draw_board += f" {string.ascii_uppercase[i]} |"
  draw_board += get_new_line()
  for row in board:
    draw_board += draw_horizontal_line(board_width + 1)
    draw_board += f"\n {current_row} |"
    for col in row:
      draw_board += f" {col} |"
    draw_board += get_new_line()
    current_row += 1
  draw_board += draw_horizontal_line(board_width + 1)
  print(draw_board)
  
print(display_board((["#", "S", "#"], ["#", "#", "#"], ["#", "#", "#"])))