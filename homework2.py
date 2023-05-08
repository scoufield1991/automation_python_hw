'''
You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
Show it in code.
Keep in mind that people with the same name can be in both companies
'''
eleks = ['Tom', 'Linda', 'Yurii']
toshiba = ['Davis', 'Linda', 'Keegan']
toshiba.extend(eleks)
new_toshiba = set(toshiba)
print(new_toshiba)

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
print(all_blacklist)

'''
You have two groups of people. 
One group consists of omnivores, the other only vegetarians. 
An omnivore is a vegetarian but a vegetarian is not an omnivore. 
Display a list of guests who can eat vegetables and herbs.
'''
omnivores = ['Dina', 'Alex', 'Loran']
vegetarians = ['Vitalka', 'Yurii', 'Arina', 'Marta']
list_guests = omnivores + vegetarians
print(list_guests)

'''
You have a group of guests for the VIP box. 
The seats in the VIP box are all occupied by these guests. 
There is a group of guests in the common room and there are still places in it. 
Display 2 groups of guests in code.
'''
list_vip = ['Tom', 'Loran', 'Woro', 'Sindy']
list_free = [None, 'Carol', 'Connor', 'Alisia', 'Nata', None, None]
print(list_free, list_vip)

'''
You have a group of people with non-unique names. 
Generate a list of non-duplicate names (you cannot use set for this task. 
If there are 2 johns in the list, you need to take only one of them. 
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
'''
non_unique_names = ['John Dow', 'John Dow', 'Marta Dow']
unique_names = list(dict.fromkeys(non_unique_names))
print(f'unique_names: {unique_names}')


