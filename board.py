import string, random

def draw_horizontal_line(width, style):
  return style * 4 * width

def get_new_line():
  return "\n"

def get_empty_board(width, height):
  board = list()
  cols = ["#"] * width
  for i in range(0, height):
    board.append(cols)
  return board

def get_solved_random_board(width, height):
    random_board = []
    calculate_total_board_places = width * height
    get_letters_for_shuffle = [*string.ascii_uppercase][0:calculate_total_board_places] * 2
    random.shuffle(get_letters_for_shuffle)
    for i in range(0, height):
      columns = []
      for j in range(0, width):
        columns.append(get_letters_for_shuffle[0])
        get_letters_for_shuffle.pop(0)
      random_board.append(columns)
    return random_board


def display_board(board):
  alphabet_letters = string.ascii_uppercase
  board_width = len(board[0])
  current_row = 1
  draw_board = "   |"
  for i in range(0, board_width):
    draw_board += f" {alphabet_letters[i]} |"
  draw_board += get_new_line()
  for row in board:
    draw_board += draw_horizontal_line(board_width + 1, "-")
    draw_board += f"\n {current_row} |"
    for col in row:
      draw_board += f" {col} |"
    draw_board += get_new_line()
    current_row += 1
  draw_board += draw_horizontal_line(board_width + 1, "-")
  print(draw_board)
  
# print(display_board((["#", "S", "#"], ["#", "#", "#"], ["#", "#", "#"])))
print(get_solved_random_board(4, 3))
