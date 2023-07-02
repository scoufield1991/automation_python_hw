class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = self.start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.end_index:
            value = self.sequence[self.current_index]
            self.current_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    my_sequence = ['a', 'b', 'c', 'd', 'e']
    my_iterator = CustomIterator(my_sequence, 1, 4)
    for item in my_iterator:
        print(item)
