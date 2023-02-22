from common import clear
from menu import menu
from board import get_empty_board, display_board

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
display_board(board)