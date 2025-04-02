"""
Written by: Gobi Mohanathas, 101117862
Team 059 Milestone 2 P4 Case 1
"""

#Imports
from T059_P2_search_modify_dataset import*
from T059_load_data import load_dataset

#Constants
COMMAND_LIST = ["L","A","R","F","Q"]

#Functions
def get_command() -> str:
    """
    Displays the user interface that shows the users what commands the user can use
    in the program. Returns the users command to the main while loop if it is in the
    "COMMAND_LIST". Otherwise it displays "No such command". The function has no parameters.

    >>>get_command()

    """
    #COMMAND_LIST = ["L","A","R","F","Q"]
    command = input("L)oad file \nA)dd book \nR)emove book \nF)ind book by title \nQ)uit \n:")
    command = command.upper()
    if command in COMMAND_LIST:
        return command
   
def program_loop() -> None:
    """
    Runs the programs main loop which allows the user to load files, add/remove/find boks, and quit 
    the program. The function has no parametes and returns None

    >>>program_loop()
    
    """
    command = ""
    book_file = None
    while command != "Q":
        command = get_command()
        if command in COMMAND_LIST:
            if command == "L":
                
                book_file = load_dataset(input("Enter a csv file: "))
                print("File loaded.")
                
                
            if book_file != None:
                    if command == "A":
                      user_title = input("Enter a title: ")
                      user_author = input("Enter an author: ")
                      user_lang = input("Enter a language: ")
                      user_rating = str(input("Enter a rating: "))
                      user_category = input("Enter a category: ")
                      user_publisher = input("Enter a publisher: ")
                      user_pageCount = str(input("Enter a page count: "))
                      user_book = (user_title, user_author, user_lang, user_rating, user_category, user_publisher, user_pageCount)
                      add_book(book_file, user_book)
                      

                    elif command == "R":
                        user_title = input("Enter a title: ")
                        user_category = input("Enter a category: ")
                        remove_book(user_title, user_category, book_file )

                    elif command == "F":
                        user_title = input("Enter a title: ")
                        find_books_by_title(book_file, user_title)
                    
            if command == "Q":
                print("End of program")
            elif book_file == None:
                print("No file loaded")
        elif command not in COMMAND_LIST :
            print("No such command")
        else:
            print("No file loaded")


#Main Script
if __name__ == "__main__":
    run_program =  program_loop()
    print(run_program)
    

   
    
   
                

