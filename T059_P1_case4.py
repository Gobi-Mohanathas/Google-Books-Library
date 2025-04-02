"""
Zi Xi Ning 101232746
milestone 1, team 059, case 4(string to tuple)
"""
import csv

def tuple_of_dictionary(filename:str)->tuple:
   """goes through the excel and make it publish the title, author, language, 
   ranting, publisher, generes and page count of each books in the excel.
   """
   open_file=open(filename,"r")
   read_filename=csv.reader(open_file)
   header = next(read_filename)
   fileinlist=[]
    
   for row in read_filename:
      books_dict = { header[1]:row[1], 
                     header[2]:row[2],
                     header[7]:row[7],
                     header[3]:row[3],
                     header[4]:row[4],
                     header[6]:row[6],
                     header[5]:row[5]}
      fileinlist.append(books_dict)
      
      fileintuple=tuple(fileinlist)   
   open_file.close()
   return fileintuple
      


filename = "Google_Books_Dataset.csv"
test_dict = tuple_of_dictionary(filename)
print(test_dict)
