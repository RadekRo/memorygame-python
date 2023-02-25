import string, random, time

def draw_horizontal_line(width, style):
  return style * 4 * width

def get_new_line():
  return "\n"

def check_status(value):
  if value == "#":
    return "free"
  else:
    return "occupied"

def get_empty_board(width, height):
  board = {}
  for i in range(0, width):
    letter = string.ascii_uppercase[i]
    for number in range(1, height + 1):
      key = letter + str(number) 
      board[key] = "#"
  return board

def get_solved_board(width, height):
  solved_board = {}
  index = 0
  calculate_board_space = int(width * height / 2)
  get_letters_for_shuffle = [*string.ascii_uppercase][0:calculate_board_space] * 2
  random.shuffle(get_letters_for_shuffle)
  for i in range(0, width):
    letter = string.ascii_uppercase[i]
    for number in range(1, height + 1):
      key = letter + str(number) 
      solved_board[key] = get_letters_for_shuffle[index]
      index += 1
  return solved_board

def display_board(board, width, height):
  alphabet_letters = string.ascii_uppercase[0:width]
  current_row = 1
  display_width = width + 1
  draw_board = "   |"
  for i in range(0, width):
    draw_board += f" {alphabet_letters[i]} |"
  draw_board += get_new_line()
  for row in range(0, height):
    draw_board += draw_horizontal_line(display_width, "-")
    draw_board += f"\n {current_row} |"
    for col in range(1, display_width):
      key = alphabet_letters[col-1] + str(current_row)
      draw_board += f" {board[key]} |"
    draw_board += get_new_line()
    current_row += 1
  draw_board += draw_horizontal_line(display_width, "-")
  print(draw_board)

def expose_tile(coords, board, solution):
  status = check_status(str(board[coords]))
  if status == "free":
    change = solution[coords]
    board[coords] = str(change)
  else:
    print("***UNLUCKY! THIS POSITION IS ALREADY UNCOVERED!***\n***TRY AGAIN! (One turn lost)***")  
    time.sleep(1.2)
  return board
  
def validate_pair(chosen_pair, board):
  return board[chosen_pair[1]] == board[chosen_pair[2]]
