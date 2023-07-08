from abc import ABC, abstractmethod


class Reader(ABC):
    def read_file(self):
        pass

    def write_file(self, text: str):
        pass
