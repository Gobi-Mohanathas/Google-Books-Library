"""
Originally written by Ben Tschakovsky, 101236275
Reviewed by:
Grant Achuzia, 101222695
Gobi Mohanathas, 101117862
ZiXi Ning, 101232746
Team 059 Milestone 1 Task 4
"""


#Imports
import csv


#Funtion
def load_dataset(filename: str) -> dict:
    """
    Returns a dictionary where the keys are genres of books, and the corresponding
    value is a list containing a dictionary for each book inside the given
    category.
    
    >>>load_dataset(filename)
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page_count': '288'}, 
    (another element),
    ...
    ],
    ...
    }
    """
    
    csv_file = open(filename, 'r') 
    csv_reader = csv.reader(csv_file) 
    header = next(csv_reader)   
    dict_1 = {} 
    
    for  row in csv_reader: 
        dict_2 = {header[1]: row[1], header[2]: row[2], header[7]: row[7], header[3]: row[3], header[4]: row[4], header[5]: row[5],}
        
        if row[6] in dict_1: 
            dict_value = dict_1.get(row[6]) + [dict_2] 
            dict_1.update({row[6]: dict_value})
        else:
            dict_1.update({row[6]: [dict_2]})
    return dict_1 



