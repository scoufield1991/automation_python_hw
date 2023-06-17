from electric_transport import ElectricTransport


class FreightTransport(ElectricTransport):

    def __init__(self, seats: int, speed: float, cargo_compartment: int):
        super().__init__(type_transport='Freight', seats=seats, speed=speed)
        self._cargo_compartment = cargo_compartment

    def __cargo_loading(self):
        print('Before start ride we need cargo loading on our transport.')
        print('Complete loading!')

    def __cargo_unloading(self):
        print('The ride is almost finished, we need cargo unloading from our transport.')
        print('Complete unloading!')

    def start_ride(self):
        self.__cargo_loading()
        print('Start riding.')

    def finish_ride(self):
        self.__cargo_unloading()
        print('Finish riding.')

    def get_information(self):
        print(f'Information about freight transport: seats = {self._seats}, speed = {self._speed}, '
              f'cargo_compartment = {self._cargo_compartment}')


if __name__ == '__main__':
    transport = FreightTransport(2, 45, 500)
    transport.start_ride()
    transport.finish_ride()
    transport.get_information()
