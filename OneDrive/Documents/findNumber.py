""" write a programme that will take the a set of numbers 
and another number then print on the screen if that number existe on the set """

""" - Write "set number" 
    - Read set number
    - Write "enter one number"
    - Read number
      Compare if number == a number of set 
      until to finish all of set number
      if number exist
         -Read a number  
      else is not exist
"""
import numpy as np

# User input

# we can do this : 
"""  numb = input("please enter a number  number click on space after click to enter")
user_list= numb.split()
list_of_numbers = []
for n in user_list:
    list_of_numbers.append(float(n))
print (list_of_numbers)  """
# or this : 
list_of_number = list(map(float, input("Write the numbers with space").split()))
print (list_of_number)
numComp= float(input("Enter the number you wantto find: "))
print(numComp)

#my find

if numComp in list_of_number:
    print("I find the number you search")
else:
    print("I didn't ")