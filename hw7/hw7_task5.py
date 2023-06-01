def own_all(object_for_checking):
    """
    Task5. Implement your own all function
    """
    for element in object_for_checking:
        if not element:
            return False
    return True


if __name__ == '__main__':
    print(own_all([1, 3, 4, 0]))
    print(own_all([1, 3, 4, 2]))
