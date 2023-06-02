"""
Find all of the numbers from 1-1000 that are divisible by 7
"""

new_list = (item for item in range(1, 1001) if item % 7 == 0)
for index in new_list:
    print(index)
