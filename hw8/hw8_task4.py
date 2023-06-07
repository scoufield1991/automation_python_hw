"""
Find all of the numbers from 1-1000 that have a 3 in them
"""

test_list = (item for item in range(1, 1001) if '3' in str(item))
for index in test_list:
    print(index)
