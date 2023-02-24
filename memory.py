from common import clear
from menu import menu
from board import get_empty_board, display_board, draw_horizontal_line
from coordinates import get_human_coordinates
from time import sleep

game_mode = menu()
clear()

match game_mode:
    case 1:
        height, width = (3, 2)
        level = "EASY"
    case 2:
        height, width = (4, 3)
        level = "MEDIUM"
    case 3:
        height, width = (5, 4)
        level = "HARD"

board = get_empty_board(height, width)
game_running = True
user_coordinates = True
turn = 1

while game_running == True:
    #info header
    print("Game level:", level)
    print("Current move:", turn)
    print("Type \033[1m'quit'\033[0m to exit the game")
    print(draw_horizontal_line(6, "="))
    #main board
    display_board(board)

    if user_coordinates == False:
        print("WRONG ENTRY! Please provide proper coordinates!")
    user_coordinates = get_human_coordinates(width)

    if user_coordinates == "quit":
        print("QUITTING THE GAME... Please wait...")
        sleep(1)
        print("GAME OVER! See you next time!")
        break
    elif user_coordinates == False:
        clear()
        continue

    turn += 1
    print("PROGRAM IS WORKING CORRECTLY")
    print(user_coordinates)
    break