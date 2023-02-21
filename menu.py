from common import clear

def menu():
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
    choice = input("Your choice?: ")

menu()