from abc import ABC, abstractmethod


class ElectricTransport(ABC):
    def __init__(self, type_transport: str, seats: int, speed: float):
        self._type_transport = type_transport
        self._seats = seats
        self._speed = speed

    @abstractmethod
    def start_ride(self):
        pass

    @abstractmethod
    def finish_ride(self):
        pass

    @abstractmethod
    def get_information(self):
        pass
