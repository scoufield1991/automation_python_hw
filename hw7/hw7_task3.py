def map_seq(callback, sequence):
    """
    Implement your own implementation of the function map
    """
    mapped_seq = []
    for element in sequence:
        mapped_seq.append(callback(element))
    return mapped_seq


def square_number(num):
    return num ** 2


def add_prefix(element):
    return type(element) == str and 'Prefix ' + element


def double_float(element):
    return type(element) == float and element * 2


if __name__ == '__main__':
    sequence_for_test_map = ['apple', 'banana']
    float_list_for_test_map = [1.5, 3.7]
    print(f'Map - working with string: {map_seq(add_prefix, sequence_for_test_map)}')
    print(f'Map - working with float: {map_seq(double_float, float_list_for_test_map)}')
    numbers_list_for_test_map = [1, 2, 3, 4, 5]
    print(f'Map - working with integer: {map_seq(square_number, numbers_list_for_test_map)}')
