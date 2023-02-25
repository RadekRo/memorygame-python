import string

def user_entry_validation(entry):
    return entry[0].isalpha() and entry[1].isdigit() and len(entry) == 2

def board_range_validation(entry, board_width, board_height):
    letters_range = [*string.ascii_uppercase[0:board_width]]
    return letters_range.count(entry[0].upper()) > 0 and int(entry[1]) <= board_height and int(entry[1]) > 0

def change_user_entry_to_key(entry):
    col = entry[0].upper()
    row = str(entry[1])
    return col + row

def get_human_coordinates(board_width, board_height):
    choice = input("Choose a card (A1, B1...) to uncover: ")
    if choice == "quit":
        return choice
    if user_entry_validation(choice) and board_range_validation(choice, board_width, board_height):
        return change_user_entry_to_key(choice)
    else:
        return False
