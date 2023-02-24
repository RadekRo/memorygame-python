from common import clear
from menu import menu
from board import get_empty_board, display_board, draw_horizontal_line
from coordinates import get_human_coordinates


game_mode = menu()
clear()

match game_mode:
    case 1:
        height, width = (3, 3)
        level = "EASY"
    case 2:
        height, width = (4, 4)
        level = "MEDIUM"
    case 3:
        height, width = (5, 5)
        level = "HARD"
board = get_empty_board(height, width)
game_running = True
user_coordinates = True
while game_running == True:
    print("Game level:", level)
    print("Current score:", level)
    print(draw_horizontal_line(6, "="))
    display_board(board)
    if user_coordinates == False:
        print("WRONG ENTRY! Please provide proper coordinates!")
    user_coordinates = get_human_coordinates(width)
    if user_coordinates == False:
        clear()
        continue
    print("PROGRAM IS WORKING CORRECTLY")
    break