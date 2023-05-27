
def square_counting(side):
    """
    2. Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
    the perimeter of the square, the area of the square, and the diagonal of the square.
    """
    diagonal = pow(side, 0.5)
    perimeter = 4 * side
    area = pow(side, 2)
    square_tuple = (perimeter, area, diagonal)
    return square_tuple


if __name__ == '__main__':
    print(square_counting(6))
