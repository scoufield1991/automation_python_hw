from abc import ABC, abstractmethod


class ITransport(ABC):

    @abstractmethod
    def _start_engine(self):
        pass

    @abstractmethod
    def _move(self, x: int, y: int):
        pass

    @abstractmethod
    def _stop_engine(self):
        pass

    @abstractmethod
    def _go_to_gus_station(self):
        pass
