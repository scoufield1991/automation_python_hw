from electric_transport import ElectricTransport


class PersonalTransport(ElectricTransport):

    def __init__(self, seats: int, speed: float, distance_per_one_charge: float, key: bool):
        super().__init__(type_transport='Personal', seats=seats, speed=speed)
        self._distance_per_one_charge = distance_per_one_charge
        self._key = key

    def __turn_on(self):
        if self._key is True:
            print('Take a key from your pocket and turn on.')
        else:
            print('Turn button "Start" on your transport.')

    def __turn_off(self):
        if self._key is True:
            print('Turn off and put your key into the pocket.')
        else:
            print('Turn button "Stop" on your transport.')

    def start_ride(self):
        self.__turn_on()
        print('Start riding on our transport.')

    def finish_ride(self):
        self.__turn_off()
        print('End riding on your transport')

    def get_information(self):
        print(f'Information about personal transport: seats = {self._seats}, speed = {self._speed}, '
              f'distance per one charge = {self._distance_per_one_charge} and key = {self._key}')


if __name__ == '__main__':
    # public = PublicTransport(35, True, 3.55)
    # public.start_ride()
    # public.finish_ride()
    personal = PersonalTransport(1, 25.5, 2, True)
    personal.start_ride()
    personal.finish_ride()
    personal.get_information()
