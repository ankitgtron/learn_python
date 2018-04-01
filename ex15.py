# 30 Jan, 2018
# 2 Feb, 2018


# This is how we import some features from the python feature set
from sys import argv
# Assigning the arguements to the two variable 
script, filename = argv
# Opening the file and assigning to the txt
txt = open(filename, 'r')
# printing f-string
print(f"Here is your file {filename}:")
# Reading the txt and printing the txt
print(txt.readlines())
# Printing 
print("Type the filename again")
# Storing the input to file_again 
file_again = input('> ')
# Opening the file and storing the file in the txt_again
txt_again = open(file_again)
# Reading the file and printing the file 
print(txt_again.read())
