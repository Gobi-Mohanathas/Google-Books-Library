#Ben Tschakovsky 101236275
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
    
    csv_file = open(filename, 'r') 
    csv_reader = csv.reader(csv_file) 
    header = next(csv_reader)   
    dictionary1 = {} 
    for  row in csv_reader: 
        dictionary2 = {header[1]: row[1], 
                  header[2]: row[2],
                  header[7]: row[7],
                  header[3]: row[3],
                  header[4]: row[4],
                  header[5]: row[5],}
    
        if row[6] in dictionary1: 
            dict_value = dictionary1.get(row[6]) + [dictionary2] 
            dictionary1.update({row[6]: dict_value})
        else:
            dictionary1.update({row[6]: [dictionary2]})
    return dictionary1 

    
    
filename = "Google_Books_Dataset.csv"
test_dict = book_category_dictionary_list(filename)
print(test_dict)   