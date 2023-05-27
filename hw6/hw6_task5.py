
def calculating_sum(*args):
    """
    6. Create a function that accepts N parameters of type int. Calculate the sum of these parameters and return it.
    """
    sum_numbers = 0
    for num in args:
        sum_numbers = sum_numbers + num
    return sum_numbers


if __name__ == '__main__':
    print(calculating_sum(1, 5, 7, 15))
