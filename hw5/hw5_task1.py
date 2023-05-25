import random
import os
import pickle
"""
1. Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
a. element is an integer that will be the left operand of the expression
b. element is an integer that will be the right operand of the expression
c. element is an integer from 1 to 3 where:
identifies the addition operation
identifies the subtraction operation
identifies the multiplication operation
d. You can put data into a text file with the text form or use the pickle module in binary form. 
If placed as text then each line should contain only elements of one tuple separated by spaces (eg "100 2 3"). 
The file must be created by a script in a pre-created \test\data directory tree. 
The directory tree must be created by the script. 
Push only the code to the repository (not directories or file).
"""
list_tuples = []
for iteration in range(100):
    left_operand = random.randint(0, 9)
    right_operand = random.randint(0, 9)
    operation_operand = random.randint(1, 3)
    list_tuples.append((left_operand, right_operand, operation_operand))

os.makedirs('./test/data')
os.chdir('./test/data')
with open('qwerty.txt', 'w+b') as file:
    data_to_write = pickle.dumps(list_tuples)
    file.write(data_to_write)
