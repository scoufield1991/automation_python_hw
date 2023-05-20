'''
you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
The element with an odd index is put into a new list of tuples where the first element is the index
and the second is the value. [(index, value)]. accordingly,
elements with an even index are placed in another list of tuples with the same format as in the case with odd indices.
'''
elements = [1, 2, 3, 4, 5, 6, 7, 8]
# elements = [1, 2, 2, 2, 4, 4, 4, 1]
list_odd_indices = []
list_even_indices = []
for index, element in enumerate(elements):
    if index % 2 == 0:
        list_even_indices.append((index, element))
    else:
        list_odd_indices.append((index, element))
print(f'list_odd_indices: {list_odd_indices}')
print(f'list_even_indices: {list_even_indices}')
