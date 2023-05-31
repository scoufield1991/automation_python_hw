
def display_box(width: int, height: int, character="*"):
    """
    Write a function with the following signature: def display_box(width: int, height: int, character="*") .
    This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width,
     using character to print the lines.
    For example, display_box(5, 4, 'x') should output the following:
    """
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(character * width)
        else:
            print(character + (' ' * (width - 2)) + character)


if __name__ == '__main__':
    display_box(10, 3)
