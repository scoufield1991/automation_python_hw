from hw13.task2.abstract_reader import Reader
from hw13.task2.abstract_writer import Writer
from hw13.task2.txt_reader import TxtReader
from hw13.task2.txt_writer import TxtWriter


class TxtProxyWriterReader(Writer, Reader):
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__reader = TxtReader(file_path)
        self.__writer = TxtWriter(file_path)
        self.__text = ''

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def write(self, text):
        self.__text = text
        self.__writer.write(text)
        self.__is_actual = False


if __name__ == '__main__':
    txt_proxy_writer_reader = TxtProxyWriterReader('data.txt')

    data = txt_proxy_writer_reader.read_file()
    new_data = txt_proxy_writer_reader.read_file()
    txt_proxy_writer_reader.write("LOL3")
    new_data = txt_proxy_writer_reader.read_file()
    new_data = txt_proxy_writer_reader.read_file()
    txt_proxy_writer_reader.write("Cool")
    new_data = txt_proxy_writer_reader.read_file()
    new_data = txt_proxy_writer_reader.read_file()
