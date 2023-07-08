from hw13.task2.abstract_reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path) as file:
            text = file.read()
        return text

    def write_file(self, new_text):
        with open(self.file_path, 'w') as file:
            file.write(new_text)

