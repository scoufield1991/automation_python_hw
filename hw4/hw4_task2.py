"""
you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""

default_list = ["FirstItem", "FriendsList", "MyTuple"]
converting_list = []
for i in default_list:
    count = 0
    for j in i:
        if not j == j.lower():
            count += 1
            if count > 1:
                i = (i[:i.index(j)] + '_' + i[i.index(j):]).lower()
                converting_list.append(i)
print(f'Convert list: {converting_list}')
