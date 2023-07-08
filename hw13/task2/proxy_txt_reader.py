from hw13.task2.abstract_reader import Reader
from hw13.task2.txt_reader import TxtReader


class TxtProxyReader(Reader):

    def __init__(self, txt_path):
        self.__result = ''
        self.__is_actual = False
        self.__reader = TxtReader(txt_path)
        self.__text = ''
        self.__writer = TxtReader(txt_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            print(self.__result)
            return self.__result

    def write_file(self, text):
        self.__text = text
        self.__writer.write_file(text)
        self.__is_actual = False


if __name__ == '__main__':
    txt_proxy_reader = TxtProxyReader('data.txt')

    data = txt_proxy_reader.read_file()
    new_data = txt_proxy_reader.read_file()
    txt_proxy_reader.write_file("LOL")
    new_data = txt_proxy_reader.read_file()
    txt_proxy_reader.write_file("Cool")
    new_data = txt_proxy_reader.read_file()
