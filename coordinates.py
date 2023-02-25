import string

def user_entry_validation(entry):
    return entry[0].isalpha() and entry[1].isdigit() and len(entry) == 2

def board_range_validation(entry, board_width):
    letters_range = [*string.ascii_uppercase[0:board_width]]
    return letters_range.count(entry[0].upper()) > 0 and int(entry[1]) <= board_width and int(entry[1]) > 0

def change_user_entry_to_coordinates(entry):
    col = string.ascii_uppercase.index(entry[0].upper())
    row = int(entry[1]) - 1
    return int(row), int(col)

def get_human_coordinates(board_width):
    choice = input("Choose a card (A1, B3...) to uncover: ")
    if choice == "quit":
        return choice
    if user_entry_validation(choice) and board_range_validation(choice, board_width):
        return change_user_entry_to_coordinates(choice)
    else:
        return False
