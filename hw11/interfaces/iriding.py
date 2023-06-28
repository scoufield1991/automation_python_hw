from abc import ABC, abstractmethod


class IRiding(ABC):

    @abstractmethod
    def _step_on_gas(self):
        pass

    @abstractmethod
    def _stop(self):
        pass

    @abstractmethod
    def _parking(self):
        pass
