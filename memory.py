from common import clear
from menu import menu
from board import get_empty_board, display_board, draw_horizontal_line, get_solved_board, expose_tile, validate_pair
from coordinates import get_human_coordinates
from time import sleep

game_mode = menu()
clear()

match game_mode:
    case 1:
        width, height = (3, 2)
        level = "EASY"
    case 2:
        width, height = (4, 3)
        level = "MEDIUM"
    case 3:
        width, height = (5, 4)
        level = "HARD"

board = get_empty_board(width, height)
solution = get_solved_board(width, height)
game_running = True
user_coordinates = True
turn = 1
current_pair = list()

while game_running == True:
    #info header
    print("Game level:", level)
    print("Current move:", turn)
    print("Type \033[1m'quit'\033[0m to exit the game")
    print(draw_horizontal_line(6, "="))
    #main board
    display_board(board, width, height)

    current_pair.append(user_coordinates)
    if turn % 2 == 1 and turn > 1:
        is_pair = validate_pair(current_pair, board)
        print(current_pair)
        if is_pair:
            print("BRAVO! A PAIR! WELL DONE!")
            sleep(1)
        else:
            first_pair = current_pair[1]
            second_pair = current_pair[2]
            board[first_pair] = "#"
            board[second_pair] = "#"
            print("UNLUCKY! NO PAIR. TRY AGAIN!")
            sleep(1)
        current_pair = []

    if user_coordinates == False:
        print("WRONG ENTRY! Please provide proper coordinates!")
    user_coordinates = get_human_coordinates(width, height)
    if user_coordinates == "quit":
        print("QUITTING THE GAME... Please wait...")
        sleep(1)
        print("GAME OVER! See you next time!")
        break
    elif user_coordinates == False:
        clear()
        continue
    board = expose_tile(user_coordinates, board, solution)
    clear()
    turn += 1