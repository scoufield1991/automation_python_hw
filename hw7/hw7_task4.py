def min_max(new_list: list):
    """
    Implement your own implementation of function max and min
    """
    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list[0], new_list[-1]


if __name__ == '__main__':
    test_list = [2, 0, 5, 1, 9, 6, 7]
    print(min_max(test_list))
