import re
"""
you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""

default_list = ["FirstItem", "FriendsList", "MyTuple"]
converting_list = []

for word in default_list:
    split_words = re.findall(r'[A-Z][^A-Z]*', word)
    converting_list.append(split_words[0].lower() + '_' + split_words[1].lower())
print(converting_list)

