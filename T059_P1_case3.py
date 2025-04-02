# Gobisangar Mohanathas, 101117862

from typing import List
import csv

def list_of_dictionaries(filename: str) -> List[dict]:
    """ Given an excel file (string), a list is returned containing multiple
    dictionaries where the first row of the file are the keys for the
    dictionary and the respective columns of the keys are the values. 
    
    >>> list_of_dictionaries("Google_Books_Dataset.csv")
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
    'author': 'Barbara Allan', 
    'rating': '3.3', 
    'publisher': 'Kensington Publishing Corp.', 
    'page_count': '288', 
    'generes': 'Fiction', 
    'language': 'English'}, 
    {next element}, ...  
    {last element}]
    """
    
    infile = open(filename)
    reader = csv.reader(infile)
    header = next(reader)
    
    book_list = []
    
    
    for column in reader:
        list_dictionary = {header[1] : column[1], header[2] : column[2],
                           header[7] : column[7], header[3] : column[3],
                           header[4] : column[4], header[6] : column[6],
                           header[5] : column[5]}
        book_list.append(list_dictionary)
        
    infile.close()
    return book_list

         

      
   