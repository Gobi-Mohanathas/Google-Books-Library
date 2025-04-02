#Gobi Mohanathas 101117862
#Case 1
#T059

import csv
#import pprint


def book_category_dictionary_list(filename: str) -> dict:
    """
    Returns a dictionary where the keys are genres of books, and the corresponding
    value is a list containing a dictionary for each book inside the given
    category.
    """
    
    book_dictionary = {} 
    
    infile = csv.DictReader(open(filename, newline=""), delimiter = ",")
    
    for row in infile: 
        books_dict = {"title":row.get("title"), 
                 "authors":row.get("author"),
                 "language":row.get("language"),
                 "rating":row.get("rating"),
                 "publisher":row.get("publisher"),
                 "PageCount":row.get("page_count"),}
       
        genre = row.get("generes") 
        
        if genre not in book_dictionary:
            book_dictionary.update({genre:[books_dict]})
        else:
            books_list = book_dictionary.get(genre)
            books_list += [books_dict]
            book_dictionary.update({genre:books_list})
    return book_dictionary

    
    
filename = "Google_Books_Dataset.csv"
test_dict = book_category_dictionary_list(filename)
#pp = pprint.PrettyPrinter(indent=4)
#print(pp.pprint(test_dict))
print(test_dict)   