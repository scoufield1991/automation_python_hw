'''
You have 2 lists of names friends = ["John", "Marta", "James"] and enemies = ["John", "Johnatan", "Artur"].
Loop through the names of friends and write the message f"{friend} we are the best friends"
if the friend is not in the list of enemy names. And display the message f"{friend} we are not friends anymore"
if the friend is on the list of enemies.
If the friend's name is James, we don't check him because he is the best friend.
'''
friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend in friends:
    if friend == 'James':
        print(f'{friend} - we are the best friends')
    elif friend in enemies:
        print(f'{friend} - we are not friends anymore')
    elif friend not in enemies:
        print(f'{friend} - we are the best friends')
