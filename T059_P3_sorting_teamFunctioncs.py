"""
Written by: Grant Achuzia, 101222695
Reviewed by:
Ben Tschakovsky, 101236275
Gobi Mohanathas, 101117862
ZiXi Ning, 101232746
Team 059 Milestone 2 P3 Team Functions ******************************************CHANGE FILE NAME DONT FORGET
"""
#Imports
from T059_load_data import load_dataset
from typing import List
from typing import Dict

#Functions

#Function 1
def sort_books_title(team059_dictionary: dict) -> list:
    """
    Written by: Grant Achuzia, 101222695
    
    Returns a list of the book data stored alphabetically in a dictionary, by title. This is made possible using the 
    "bubble sort" algorithm.
    
    >>>sort_books_title()

    """
    
    book_list = []
    new_dictionary = {}
    
    for category in team059_dictionary.keys():
        for book in team059_dictionary.get(category):
            new_dictionary = book
            new_dictionary.update({"genres": category})
            book_list.append(new_dictionary)
    
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]["title"] > book_list[j+1]["title"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
        return book_list
    
    print(sort_books_title(load_dataset("Google_Books_Dataset.csv")))
#------------------------------------------------------------------------------------------------------------------------------------  
#Function 2
def sort_books_ascending_rate(dictionary: dict)-> list:
    """
    Takes input dictionary and returns a list of the books in ascending
    order according to their rate.
    """
    new_list = []
    new_dict = {}
    
    for book in dictionary:
        for r in dictionary[book]:
            new_dict = r
            new_dict.update({"generes": book})
            new_list.append(new_dict)
        
    L = len(new_list)           
             
    for i in range(L):
        for j in range(0, L-i-1):
            if new_list[j]["rating"] > new_list[j+1]["rating"]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    
    for i in range(L):
        if new_list[i]["rating"] == '':
            new_list[i]["rating"] = '0'     
     
    for i in range(len(new_list)):
        print(new_list[i]["title"], new_list[i]["rating"])           
       
    return new_list
#------------------------------------------------------------------------------------------------------------------------------------  
#Function 3
def sort_books_descending_rate(dictionary: dict)-> list:
    """
    Takes input dictionary and returns a list of the books in ascending
    order according to their rate.
    """
    new_list = []
    new_dict = {}
    
    for book in dictionary:
        for r in dictionary[book]:
            new_dict = r
            new_dict.update({"generes": book})
            new_list.append(new_dict)
    
    L = len(new_list)
    for i in range(L):
        if new_list[i]["rating"] == '':
            new_list[i]["rating"] = '0' 
            
    for i in range(L):
        for j in range(0, L-i-1):
            if new_list[j]["rating"] < new_list[j+1]["rating"]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
                        
    for i in range(len(new_list)):
        print(new_list[i]["title"], new_list[i]["rating"])     
           
    return new_list
#------------------------------------------------------------------------------------------------------------------------------------  
#Function 4
def sort_books_publisher(team059_dictionary: dict) -> list :
    """
    Written by: Gobi Mohanathas, 101117862
     
    Returns a list of the book data stored alphabetically in a dictionary, by publisher. This is made possible using the 
    "bubble sort" algorithm.
    
    >>>sort_books_publisher()
    """
    
    book_list = []
    new_dictionary = {}
    
    for category in team059_dictionary.keys():
        for book in team059_dictionary.get(category):
            new_dictionary = book
            new_dictionary.update({"genres": category})
            book_list.append(new_dictionary)
    
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]["publisher"] > book_list[j+1]["publisher"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    
    new_list = []
    for book in book_list:
        if book["publisher"] != "":
            new_list += [book]
    return new_list
#------------------------------------------------------------------------------------------------------------------------------------  
#Function 5
def sort_books_pageCount(dictionary: dict) -> List[dict]:
    
    """ Given the dictionary containing the Google Books, the function will
    return a list of dictionaries containing the book's data. The books will be
    arranged in order of ascending page count. If the books have equivalant page
    count then they are sorted alphabetically. Additionally a print message will
    list out the title and page count of the books in ascending order.
    
    >>> sort_books_pageCount(dictionary)
    The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further 30
    The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further 30
    The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further 30
    The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further 30
    The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further 30
    We Should All Be Feminists 32
    ..... (to indicate some books have been skipped over)
    Business Strategy (The Brian Tracy Success Library) 112
    Business Strategy (The Brian Tracy Success Library) 112
    Management (The Brian Tracy Success Library) 112
    Management (The Brian Tracy Success Library) 112
    .....
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire) 4544
    
    * If called through the Python shell, it will also show the returned list:
    
    [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'language': 'English', 'rating': '0', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': '14', 'genres': 'Economics'},
    {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'language': 'English', 'rating': '0', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': '14', 'genres': 'Business'},
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English', 'rating': '3.7', 'publisher': 'Hachette UK', 'page_count': '30', 'genres': 'Economics'},
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English', 'rating': '3.7', 'publisher': 'Hachette UK', 'page_count': '30', 'genres': 'Business'},
    ..... 
    {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': 'English', 'rating':
    '4.5', 'publisher': 'HarperCollins UK', 'page_count': '4544', 'genres': 'Epic'}]
    
    (On the shell it will show it in a single line, I have shown it this way for
     a "cleaner" look)
    """
    
    book_list = []
    new_dict = {}
    
    for category in dictionary.keys():
        for book in dictionary.get(category):
            new_dict = book
            new_dict.update({"genres" : category})
            book_list.append(new_dict)      
     
    n = len(book_list)

    for i in range(n):        
        for j in range(0, n-i-1):
            if int(book_list[j]["page_count"]) > int(book_list[j+1]["page_count"]):
                    book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
                    
    for i in range(n):
        for j in range(0, n-i-1):
            if int(book_list[j]['page_count']) == int(book_list[j+1]["page_count"]) and book_list[j]["title"] > book_list[j+1]["title"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
                
    for i in range(n):
        if book_list[i]["rating"] == '':
                book_list[i]["rating"] = '0'
          
    for i in range(len(book_list)):
        print(book_list[i]["title"], book_list[i]["page_count"])
        
        # After consulting several TA's regarding what should be printed for the
        # function, I was informed it was enough to print just the titles and
        # the page count asscoiated with the title.
        
    return book_list
#------------------------------------------------------------------------------------------------------------------------------------  
#Function 6
def sort_books_category(dictionary: dict) -> list:
    
    book_list = []
    new_dict = {}
        
    for category in dictionary.keys():
        for book in dictionary.get(category):
            new_dict = book
            new_dict.update({"genres" : category})
            book_list.append(new_dict)
    print(book_list)
    
    n = len(book_list)
    
    for i in range(n):        
        for j in range(0, n-i-1):
            if book_list[j]["genres"] > book_list[j+1]["genres"]:
                    book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]['genres'] == book_list[j+1]['genres'] and book_list[j]['title'] > book_list[j+1]['title']:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]  
    for i in range(len(book_list)):
        print(book_list[i]["title"], book_list[i]["genres"])    
        
    return book_list