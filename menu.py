from common import clear

def get_user_choice():
    choice = int(input("Your choice?: "))
    return choice

def menu():
    valid_user_entry = False
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
        user_entry = get_user_choice()
        valid_user_entry = True if user_entry > 0 and user_entry < 5 else False
    return user_entry
print(menu())