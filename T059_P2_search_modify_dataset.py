"""
Written by: Grant Achuzia, 101222695
Reviewed by: 
Ben Tschakovsky, 101236275
Gobi Mohanathas, 101117862
ZiXi Ning, 101232746
Team 59 Milestone 1 P2 Task 3, All Functions
Disclaimer: To homogenize our work for this file, we decided to switch the name of the dictionary that calls load_dataset "team059_dictionary", in individual functions this may not be the case.
"""
from T059_load_data import load_dataset

#Function 1
def print_dictionary_category(category: str, team059_dictionary: dict) -> int:
    """
    Written by: Grant Achuzia, 101222695
     
    Returns the number of elements (books) associated with the key ("categories") in the dictionary given the category and the dictionary.
    
    >>>print_dictionary_category("Fiction", load_dataset("Google_Books_Dataset.csv"))
    39
    >>>print_dictionary_category("Comics", load_dataset("Google_Books_Dataset.csv"))
    7
    >>>print_dictionary_category("Fantasy", load_dataset("Google_Books_Dataset.csv"))
    15
    
    """

    book_count = len(team059_dictionary[category])
    print("The category", category, "has", book_count, "books. This is the list of books in the category category", str(category) + ":")
    for book in team059_dictionary[category]:
        print(book)
    return book_count


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 2
def add_book(team059_dictionary: dict, my_tuple: tuple) -> dict:
    """
    Returns an updated dictionary after a book (my_tuple) has been added to the existing dictionary (load_dataset). It verifies if the book has been added through the use of a printed message.
    
    >>>add_book(load_dataset("Google_Books_Dataset.csv"),("The Foundation", "Isaac Asimov", "English", "Gnome Press", "Fiction", "4.2", "255" ))
    
    >>>add_book(load_dataset("Google_Books_Dataset.csv"),("The Three Body Problem", "Liu Cixin", "Chinese", "Chongqing Press", "Fiction", "4.1", "302"))
    
    >>>add_book(load_dataset("Google_Books_Dataset.csv"), ("Rebecca", "Daphne du Maurier", "English", "	Victor Gollancz Ltd", "Mystery", "4.2", "130" ))
    

    """
    category = my_tuple[4]
    keys = team059_dictionary.keys()
    books = team059_dictionary.get(category)
    
    for key in keys:
        if category == key:
            new_book = {'title': my_tuple[0], 'author': my_tuple[1], 'language': my_tuple[2], 'rating': my_tuple[3], 'publisher':my_tuple[5], 'page_count': my_tuple[6]} 
        
    if new_book in books:
        print('There is an error adding the book')
        
    else: 
        books.append(new_book)
        print('The book has been added correctly')
            
    return team059_dictionary   
 


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 3
def remove_book(book_title:str, category:str, team059_dictionary: dict) -> dict:
    """
    Written by: Grant Achuzia, 101222695
     
    Returns an updated dictionary with a printed message stating whether the book was removed successfully, given the title of the book, its category and the dictionary wherein the book is to be removed from.

    >>>remove_book("The Painted Man (The Demon Cycle, Book 1)","Fiction",team059_dictionary )
    The book has been removed successfully
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page_count': '288'},
    **BOOK WAS HERE**
    {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': '4.8', 'publisher': 'Tor Books', 'page_count': '226'}
    
    >>>remove_book("Edgedancer: From the Stormlight Archive", "Fiction", team059_dictionary)
    The book has been removed successfully
    {'Fiction': [
    ...
    {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page_count': '544'},
    **BOOK WAS HERE** 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'page_count': '400'}
    ...
    ]
    
    >>>remove_book("qwertyuio", "Fiction", team059_dictionary)
    There is an error removing the book. Book not found.
    **Original dictionary is printed**
    
    """
    
    books = team059_dictionary.get(category)

    for book in books:
        if book_title == book.get("title"):
            team059_dictionary[category].remove(book)
            print("The book has been removed successfully")
            return team059_dictionary
        
    else:
        print("There was an error removing the book. Book not found.")
        
    return team059_dictionary


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 4
def get_books_by_rate(team059_dictionary: dict, rate: int)-> dict:
    """
    Written by: Ben Tschakovsky, 101236275
    
    Returns a dictionary containing all the books for the rate passed through
    the function.
    >>>get_books_by_rate(team059_dictionary, 2):
    {}
    
    >>>get_books_by_rate(team059_dictionary, 3):
    Title: Antiques Roadkill: A Trash 'n' Treasures Mystery
    Author: Barbara Allan
    Rating: 3.3
    Language: English
    Publisher: Kensington Publishing Corp.
    Category: Fiction
    Page Count: 288
    ...
    Title: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further
    Author: Alvin Hall
    Rating: 3.7
    Language: English
    Publisher: Hachette UK
    Category: Investing
    Page Count: 30
    
    >>>get_books_by_rate(team059_dictionary, 4):
    Title: The Painted Man (The Demon Cycle, Book 1)
    Author: Peter V. Brett
    Rating: 4.5
    Language: English
    Publisher: HarperCollins UK
    Category: Fiction
    Page Count: 544
    ...
    Title: Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt
    Author: Adam Kay
    Rating: 4.7
    Language: English
    Publisher: Pan Macmillan
    Category: Humor 
    Page Count: 112
    """
    book_dict = {}
    lower = rate
    upper = rate + 1
    for book in team059_dictionary:
        for r in team059_dictionary[book]:
            if len(r.get("rating")) != 0 and lower <= float(r.get("rating")) < upper:
                print("Title:", r["title"])
                print("Author:", r["author"])
                print("Rating:", r["rating"])
                print("Language:", r["language"])
                print("Publisher:", r["publisher"])
                print("Category:", book)
                print("Page Count:", r["page_count"])
                book_dict[book] = r                
                        
    return book_dict

#-------------------------------------------------------------------------------------------------------------------------------------
#Function 5
def find_books_by_title(team059_dictionary: dict, title: str) -> bool:
    """
    Written by: Ben Tschakovsky, 101236275
    
    Takes the title of the book and returns a boolean variable which is 
    'True', along with the message "The book has been found", if the title is 
    in the dictionary and 'False', along with the message, "The book has not 
    been found", if it does not exist in the dictionary.
    (title must be written EXACTLY as seen in file 'Google_Books_Dataset'
    
    >>>find_books_by_title(team059_dictionary, 'Deadpool Kills the Marvel Universe') 
    The book has been found
    True
    
    >>>find_books_by_title(team059_dictionary, 'nuggest') 
    The book has NOT been found
    False
    
    >>>find_books_by_title(team059_dictionary, 'In Dark Company: A Kate Burkholder Short Story')
    """
    for category in team059_dictionary:
        for book in team059_dictionary[category]:
            if title == book["title"]:
                print("The book has been found")
                return True 
    print("The book has NOT been found")
    return False

#-------------------------------------------------------------------------------------------------------------------------------------
#Function 6
def get_books_by_author(team059_dictionary: dict, author: str) -> list:
    """
    Written by: Ben Tschakovsky, 101236275
    
    Returns all the books written by the author passed through 
    the function. (Author's name must be written EXACTLY as seen in the file
    'Google_Books_Dataset'
    
    >>>get_books_by_author(team059_dictionary, 'Barbara Allan')
    The author Barbara Allan has published the following books:
    1 - Antiques Roadkill: A Trash 'n' Treasures Mystery
    2 - Antiques Con
    3 - Antiques Chop
    4 - Antiques Knock-Off
    ["Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Antiques Con', 'Antiques Chop', 'Antiques Knock-Off']
    
    >>>get_books_by_author(team059_dictionary, 'Agatha Christie') 
    The author Agatha Christie has published the following books:
    1 - The Red Signal: An Agatha Christie Short Story
    2 - And Then There Were None
    3 - The Mysterious Affair at Styles
    ['The Red Signal: An Agatha Christie Short Story', 'And Then There Were None', 'The Mysterious Affair at Styles']
    
     >>>get_books_by_author(team059_dictionary, 'Peter V. Brett') 
     The author Peter V. Brett has published the following books:
     1 - The Painted Man (The Demon Cycle, Book 1)
     ['The Painted Man (The Demon Cycle, Book 1)']
    """
    
    books_lst = []
    
    print("The author", author, "has published the following books:")
    
    for category in team059_dictionary:
        for book in team059_dictionary[category]: 
            if author == book['author'] and book['title'] not in books_lst:
                books_lst.append(book['title'])
    count = 0 
   
    for x in books_lst:
        count += 1
        print(count, '-', x)  
        
    return books_lst  


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 7
def get_books_by_publisher(publisher: str, team059_dictionary: dict) -> list[str]:
    
    """ 
    Written by: Gobi Mohanathas, 101117862
    
    Given the publisher's name (string) and the dictionary containing the
    stored google books, a list is returned containing all the books made by
    the publisher within the dictionary. Additionally a message will print,
    "The publisher  **** (publisher name)  has published the following books:",
    along with the books published by the publisher in numbered pair.
       
    Precondition: The publishers name must exist within the excel file and be
    spelled exactly as seen.
    
    >>> get_books_by_publisher('AMACOM', team059_dictionary)
    The publisher  AMACOM  has published the following books:
    1- Marketing (The Brian Tracy Success Library)
    2- Management (The Brian Tracy Success Library)
    3- Business Strategy (The Brian Tracy Success Library)
    4- Personal Success (The Brian Tracy Success Library)
    5- The Essentials of Finance and Accounting for Nonfinancial Managers
    
    * If called through the Python shell, it will also show the returned list:
    
    ['Marketing (The Brian Tracy Success Library)', 
    'Management (The Brian Tracy Success Library)', '
    Business Strategy (The Brian Tracy Success Library)', 
    'Personal Success (The Brian Tracy Success Library)', 
    'The Essentials of Finance and Accounting for Nonfinancial Managers']
    
    (On the shell it will show it in a single line, I have shown it this way for
     a "cleaner" look)
     
     >>> get_books_by_publisher('HarperCollins Leadership', team059_dictionary)
     The publisher  HarperCollins Leadership  has published the following books:
     1- Platform: Get Noticed in a Noisy World
     2- Selling 101: What Every Successful Sales Professional Needs to Know

     >>> get_books_by_publisher('Kensington Publishing Corp.', team059_dictionary)
     The publisher  Kensington Publishing Corp.  has published the following books:
     1- Antiques Roadkill: A Trash 'n' Treasures Mystery
     2- Antiques Knock-Off
     
    """
       
       
    publisher_list = []
    
    for category in team059_dictionary.keys():
        for book in team059_dictionary.get(category):
            if book.get("publisher") == publisher:
                if book.get("title") not in publisher_list:
                    publisher_list.append(book.get("title"))
                    
    print("The publisher ", publisher, " has published the following books:")
    
    for i in range(len(publisher_list)):
        print(i + 1, end = '- ')
        print(publisher_list[i])
    
    return publisher_list


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 8
def check_category_and_title(category: str, title: str, team059_dictionary: dict) -> bool:
    
    """ 
    Written by: Gobi Mohanathas, 101117862
       
    Given the category (string), title (string), and the dictionary
    containing the google books, the function will return True along with a
    "book is in category" message if the book is in the category, otherwise
    returns False with a "book is not in category" message.
    
    Precondition: The category must exist within the excel file and be spelled
    exactly as seen.
    
    >>> check_category_and_title('Mystery', 'The Black Box', team059_dictionary)
    The category Mystery has the book title The Black Box
    True <- (This will appear if called using the shell)
    
    >>>check_category_and_title('Fiction', 'Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)', team059_dictionary)
    The category Fiction has the book title Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)
    True
    
    >>> check_category_and_title('Mystery', 'asgasdg', team059_dictionary)
    The category Mystery does not have the book title asgasdg
    False

    """
    
    for book in team059_dictionary.get(category):
        if book.get("title") == title:
            print("The category", category, "has the book title", title)
            return True
    
    print("The category", category, "does not have the book title", title)
    return False

#-------------------------------------------------------------------------------------------------------------------------------------
#Function 9
def all_categories_for_book_title(title: str, team059_dictionary: dict) -> list[str]: 
    
    """ 
    Written by: Gobi Mohanathas, 101117862
       
    Given a title (string) and the dictionary containing the google books,
    a list is returned containing all the categories for a particular book
    title. Additionally a message will print,"The book title  **** 
    (title of book)  has the following categories:", along with the categories 
    for the book in numbered pair. If the title of the book is not any category 
    an empty list will be returned with same message as before.
    
    Precondition: The title of the book must be spelled exactly as seen in the
    excel file.
    
    >>> all_categories_for_book_title('Sword of Destiny: Witcher 2: Tales of the Witcher', load_dataset("Google_Books_Dataset.csv"))
    The book title Sword of Destiny: Witcher 2: Tales of the Witcher has the following categories:
    1- Fiction
    2- Adventure
    3- Mythical Creatures
    ['Fiction', 'Adventure', 'Mythical Creatures']   <-(Will appear if called through shell)
    
    >>> all_categories_for_book_title('asdfggs', team059_dictionary)
    The book title asdfggs has the following categories:
    []    
    
    >>> all_categories_for_book_title('Little Girl Lost: A Lucy Black Thriller', team059_dictionary)
    1- Fiction
    2- Thrillers
    3- Mystery
    """
    category_list = []
    
    for category in team059_dictionary.keys():
        for book in team059_dictionary.get(category):
            if book.get("title") == title:
                if category not in category_list:
                    category_list.append(category)
                    
    print("The book title", title, "has the following categories:")
    
    for i in range(len(category_list)):
        print(i + 1, end = "- ")
        print(category_list[i])
                    
    return category_list

#-------------------------------------------------------------------------------------------------------------------------------------
#Function 10
def get_books_by_category(team059_dictionary:dict, category:str)->list:
    """
    Written by: ZiXi Ning, 101232746
    
    By choosing the category of the book, it will returns all the necessary books needed.
   
    >>>get_books_by_category(team059_dictionary,"Adventure")
    1- Sword of Destiny: Witcher 2: Tales of the Witcher
    2- A Feast for Crows (A Song of Ice and Fire, Book 4)
    3- After Anna
    4- The Way Of Shadows: Book 1 of the Night Angel
    5- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6- Edgedancer: From the Stormlight Archive
    7- The Malady and Other Stories: An Andrzej Sapkowski Sampler
    ['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']
   
    >>>get_books_by_category(team059_dictionary,"Fiction")
    The category Adventure has the following books:
    1- Sword of Destiny: Witcher 2: Tales of the Witcher
    2- A Feast for Crows (A Song of Ice and Fire, Book 4)
    3- After Anna
    4- The Way Of Shadows: Book 1 of the Night Angel
    5- A Game of Thrones: The Story Continues Books 1-5: A  Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6- Edgedancer: From the Stormlight Archive
    7- The Malady and Other Stories: An Andrzej Sapkowski Sampler
    
    >>>get_books_by_category(team059_dictionary,"Economics")
    The category Economics has the following books:
    1- How To Win Friends and Influence People
    ...
    22- Platform: Get Noticed in a Noisy World
    """   
    print("The category", category, "has the following books:")
    list1 = []
    for row in team059_dictionary:
        if category == row:
            list_of_book = team059_dictionary.get(category)
    for i in list_of_book:
        t = i["title"]
        list1.append(t)
    for a in range(len(list1)):
        print(a + 1, end = "- ")
        print(list1[a])
   
    return list1

#-------------------------------------------------------------------------------------------------------------------------------------
#Function 11
def get_book_by_category_and_rate(team059_dictionary:dict, category:str, rate:int)->list:
    """
    Written by: ZiXi Ning, 101232746
    
    Returns all the books that have the described category and rate
   
    >>>get_book_by_category_and_rate(team059_dictionary, "Adventure", 4)
    1- Sword of Destiny: Witcher 2: Tales of the Witcher
    2- A Feast for Crows (A Song of Ice and Fire, Book 4)
    3- After Anna
    4- The Way Of Shadows: Book 1 of the Night Angel
    5- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6- Edgedancer: From the Stormlight Archive
    7- The Malady and Other Stories: An Andrzej Sapkowski Sampler
    ['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']
    
    >>>get_book_by_category_and_rate(team059_dictionary, "Business", 3)
    The category Business and rate 3 have the books:
    1- How to Understand Business Finance: Edition 2
    2- The Infinite Game
    3- Selling 101: What Every Successful Sales Professional Needs to Know
    4- The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further
    ['How to Understand Business Finance: Edition 2', 'The Infinite Game', 'Selling 101: What Every Successful Sales Professional Needs to Know', 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further']

    
    >>>get_book_by_category_and_rate(team059_dictionary, "Fiction", 5)
    The category Fiction and rate 5 have the books:
    1- Final Option: 'The best one yet'
    2- The Red Signal: An Agatha Christie Short Story
    ["Final Option: 'The best one yet'", 'The Red Signal: An Agatha Christie Short Story']

    """
    list1=[]
    print("The category " + str(category) + " and rate " + str(rate) + " have the books:" )
    list2=team059_dictionary.get(category)
    for u in list2:
        if u.get("rating") != '':
            if int(float(u.get("rating")))==rate:
                t=u["title"]
                list1.append(t)   
    for a in range(len(list1)):
        print(a+1, end="- ")
        print(list1[a])   
    return list1


#-------------------------------------------------------------------------------------------------------------------------------------
#Function 12
def get_author_categories(team059_dictionary:dict, author:str)->list:
    """
    Written by: ZiXi Ning, 101232746
     
    Returns a list of all the categories the author has wrote, given the author's name as a string.
    
    >>>get_author_categories(team059_dictionary, "Blake Pierce")
    1- Fiction
    2- Detective
    3- Thrillers
    4- Mystery
    ['Fiction', 'Detective', 'Thrillers', 'Mystery']
    
    >>>get_author_categories(team059_dictionary, "Billy Connolly")
    1- Humor
    2- Biography
    ['Humor', 'Biography']
    
    >>>get_author_categories(team059_dictionary, "David Baldacci")
    1- Fiction
    2- Crime
    3- Thrillers
    4- Mystery
    ['Fiction', 'Crime', 'Thrillers', 'Mystery']
    """
    list1 = []
    for category in team059_dictionary.keys():
        for book_in_the_category in team059_dictionary.get(category):
            
            if book_in_the_category["author"]==author:
               
                if not category in list1:
                    list1.append(category)
    for a in range(len(list1)):
        print(a + 1, end ="- ")
        print(list1[a])
    return list1





