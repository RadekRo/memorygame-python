from common import clear

def get_user_choice():
    choice = int(input("Your choice?: "))
    return choice

def menu():
    valid_user_entry = False
    error_message = False
    while valid_user_entry == False:
        clear()
        print("""#     # ####### #     # ####### ######  #     # 
##   ## #       ##   ## #     # #     #  #   #  
# # # # #       # # # # #     # #     #   # #   
#  #  # #####   #  #  # #     # ######     #    
#     # #       #     # #     # #   #      #    
#     # #       #     # #     # #    #     #    
#     # ####### #     # ####### #     #    #         
==============================================
Developed by RadekRo. Version 1.23. 
==============================================
Choose a difficulty level:
1. EASY
2. MEDIUM
3. HARD
4. QUIT""")
        print("WRONG ENTRY *** ENTER VALID NUMBER (1-4)!") if error_message == True else None
        user_entry = get_user_choice()
        valid_user_entry = True if user_entry > 0 and user_entry < 5 else False
        error_message = True
        if user_entry == 4:
            print("You've chosen to QUIT the game. Bye, bye!")
            break
    return user_entry
