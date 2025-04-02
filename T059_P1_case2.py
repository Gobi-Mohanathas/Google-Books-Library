
"""
Name and Student ID: Grant Achuzia, 101222695
Team 059, Milestone 1 Project 1 Case 2 Function
"""
#Imports
import csv #contains the reader that will load the csv file


#Functions
def book_dictionary_publisher_list(filename:str) -> dict:
    """
    Returns the contents of the csv file as a dictionary that uses the publisher as its key when searching through the dictionary.
    
    >>>
    """
    csv_file = open(filename, 'r') 
    csv_reader = csv.reader(csv_file) 
    header = next(csv_reader)     
    dict_1 = {} 

    for  row in csv_reader: 
        dict_2 = {header[1]: row[1], 
                  header[2]: row[2],
                  header[7]: row[7],
                  header[3]: row[3],
                  header[6]: row[6],
                  header[5]: row[5],}
    
        if row[4] in dict_1: 
            dict_value = dict_1.get(row[4]) + [dict_2]  
            dict_1.update({row[4]: dict_value})
        else:
            dict_1.update({row[4]: [dict_2]})
    return dict_1 
            
