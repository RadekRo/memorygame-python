import string, random

def draw_horizontal_line(width, style):
  return style * 4 * width

def get_new_line():
  return "\n"

def get_empty_board(width, height):
  board = {}
  for i in range(0, width):
    letter = string.ascii_uppercase[i]
    for number in range(1, height + 1):
      key = letter + str(number) 
      board[key] = "#"
  print(board)

def get_solved_board(width, height):
  random_board = {}
  index = 0
  calculate_board_space = int(width * height / 2)
  get_letters_for_shuffle = [*string.ascii_uppercase][0:calculate_board_space] * 2
  random.shuffle(get_letters_for_shuffle)
  for i in range(0, width):
    letter = string.ascii_uppercase[i]
    for number in range(1, height + 1):
      key = letter + str(number) 
      random_board[key] = get_letters_for_shuffle[index]
      index += 1
  return random_board

def uncover_tiles(coordinates, board, solution, turn):
  row = coordinates[0]
  col = coordinates[1]
  print(row, col)
  board[row][col] = solution[row][col]
  return board

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
  
get_empty_board(4,3)
get_solved_board(4,3)