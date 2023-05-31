
def removing_vowels(word: str):
    """
    7. Write a function that takes in a string and returns the string with all the vowels removed.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = ''
    for index in word:
        if index.lower() not in vowels:
            new_word = new_word + index
    return new_word


if __name__ == '__main__':
    print(removing_vowels('AmaZing'))
