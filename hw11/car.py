from hw11.interfaces.iriding import IRiding
from hw11.interfaces.itransport import ITransport
from time import time, sleep


# Abstraction
# Inheritance

class Car(IRiding, ITransport):

    def __init__(self, liters_in_gas_tank: int):
        self.__engine_status = False
        self.__liters_in_gas_tank = liters_in_gas_tank
        self.__liters_per_one_ride = 45
        self.__car_stopped = True
        self.__x = 0
        self.__y = 0

    # Hiding
    def __reset_coordinates(self):
        self.__x = 0
        self.__y = 0

    # Polymorphism
    def _step_on_gas(self):
        self.__car_stopped = False
        print('The car started.')

    # Polymorphism
    def _stop(self):
        self.__car_stopped = True
        print('The car stopped.')

    # Polymorphism
    def _parking(self):
        print('Parking near my house!!!')

    # Polymorphism
    def _start_engine(self):
        self.__engine_status = True
        print('Engine started')

    # Polymorphism
    def _go_to_gus_station(self):
        print('We need some fuel, so we are at gas station')
        self.__liters_in_gas_tank = 100

    # Encapsulation + Polymorphism
    def _move(self, x: int, y: int):
        if self.__liters_in_gas_tank < self.__liters_per_one_ride:
            self._go_to_gus_station()
        while self.__x != x or self.__y != y:
            if self.__x != x:
                self.__x += 1
            if self.__y != y:
                self.__y += 1
            sleep(0.1)
            print('Still riding')

    # Polymorphism
    def _stop_engine(self):
        self.__engine_status = False
        print('Engine stopped.')

    # Encapsulation
    def ride_to_the_house(self, x: int, y: int):
        start_time = time()
        self._start_engine()
        self._step_on_gas()
        self._move(x, y)
        self._parking()
        self._stop()
        self._stop_engine()
        finish_time = time()
        print(f'I am riding for {finish_time - start_time}.')
        self.__reset_coordinates()
        self.__liters_in_gas_tank -= self.__liters_per_one_ride
        print(f'Now in our gus tank are {self.__liters_in_gas_tank} liters!')


if __name__ == '__main__':
    car = Car(35)
    car.ride_to_the_house(17, 20)
