from common import clear
from menu import menu
from board import get_empty_board, display_board, draw_horizontal_line

def user_move():
    choice = input("Choose a card (A1, B3...) to uncover: ")
    return choice[0].isalpha() and choice[1].isdigit()

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
print("Game level:", level)
print("Current score:", level)
print(draw_horizontal_line(6, "="))
display_board(board)
print(user_move())