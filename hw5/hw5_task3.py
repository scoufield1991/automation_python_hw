"""
3. You have the file text.txt(attached). Please count how many times each letter appears in this file.
"""
with open('text.txt') as file:
    data = file.read()

character_counts = {}
for char in data:
    if char.isalpha():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
print("Character counts:")
for char, count in character_counts.items():
    print(char, ":", count)
