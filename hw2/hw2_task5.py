'''
You have a group of people with non-unique names.
Generate a list of non-duplicate names (you cannot use set for this task.
If there are 2 johns in the list, you need to take only one of them.
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
'''
non_unique_names = ['John Dow', 'John Dow', 'Marta Dow']
unique_names = list(dict.fromkeys(non_unique_names))
print(f'unique_names: {unique_names}')