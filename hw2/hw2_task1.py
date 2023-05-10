'''
You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
Show it in code.
Keep in mind that people with the same name can be in both companies
'''
eleks = ['Tom', 'Linda', 'Yurii']
toshiba = ['Davis', 'Linda', 'Keegan']
toshiba.extend(eleks)
eleks.clear()
new_toshiba = set(toshiba)
print(f'Toshiba: {new_toshiba}')
print(f'Eleks: {eleks}')
