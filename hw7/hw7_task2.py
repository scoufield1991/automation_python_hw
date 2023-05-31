def filter_seq(callback, sequence):
    """
    task2 Implement your realization of the function filter
    """
    filtered_seq = []
    for element in sequence:
        if callback(element):
            filtered_seq.append(element)
    return filtered_seq


def is_positive(num):
    return num > 0


def starts_with_a(element):
    return type(element) == str and element.startswith('a')


def is_positive_float(element):
    return type(element) == float and element > 0


if __name__ == '__main__':
    sequence = ['apple', 'banana', 1.5, 0, 'avocado', 3.7]
    print(f'Filter - work with string: {filter_seq(starts_with_a, sequence)}')
    print(f'Filter - Work with float: {filter_seq(is_positive_float, sequence)}')
    numbers = [1, -2, 3, -4, 5]
    print(f'Filter - work with integers: {filter_seq(is_positive, numbers)}')
