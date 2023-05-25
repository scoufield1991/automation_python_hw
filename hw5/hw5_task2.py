import os
import pickle

"""
2. Using the created file in task 1, read the file and perform mathematical operations on each element.
Output the result of the operation to the console.
You cannot use imports to import from the first task module.
"""
os.chdir('./test/data')
with open('qwerty.txt', 'r+b') as file:
    byte_text = file.read()
result_list = pickle.loads(byte_text)
print(f'List of tuples from the file: {result_list}')
for index in result_list:
    if index[2] == 1:
        print(f'Addition = {index[0] + index[1]}')
    elif index[2] == 2:
        print(f'Subtraction = {index[0] - index[1]}')
    elif index[2] == 3:
        print(f'Multiplication = {index[0] * index[1]}')
