'''
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
Names of people in the format "John Dow" first and second name.
Find those who are on all blacklists.
'''
casino_blacklist = {'John Dow', 'Amanda Tilman', 'Cooper Hummel'}
poker_blacklist = {'Sandro Cortes', 'Lisandro Lopes', 'John Dow'}
alcohol_blacklist = {'John Snow', 'John Dow', 'Josh Dow'}
temp_set = casino_blacklist.intersection(poker_blacklist)
all_blacklist = temp_set.intersection(alcohol_blacklist)
print(f'In blacklist: {all_blacklist}')
