from electric_transport import ElectricTransport


class PublicTransport(ElectricTransport):

    def __init__(self, seats: int, speed: float, conductor_availability: bool, ticket_cost: float,
                 start_station: str, end_station: str):
        super().__init__(type_transport='Public', seats=seats, speed=speed)
        self._conductor_availability = conductor_availability
        self._ticket_cost = ticket_cost
        self._start_station = start_station
        self._end_station = end_station

    def __enter_transport(self):
        print(f'I am entering the transport at station {self._start_station}')

    def __pay_for_ticket(self):
        if self._conductor_availability is True:
            print(f'I give to conductor {self._ticket_cost} .')
        else:
            print(f'I will use e-ticket service and pay {self._ticket_cost} .')

    def __announcement_my_station(self):
        print(f'Next station {self._end_station} is mine')

    def start_ride(self):
        self.__enter_transport()
        self.__pay_for_ticket()

    def finish_ride(self):
        self.__announcement_my_station()
        print('I am at my station')

    def get_information(self):
        print(f'Information about public transport: seats = {self._seats}, speed = {self._speed}, '
              f'conductor availability = {self._conductor_availability} and ticket_cost = {self._ticket_cost}')


if __name__ == '__main__':
    public = PublicTransport(35, 50, False, 3.55, 'Balzak street', 'Miloslavskaya street')
    public.start_ride()
    public.finish_ride()
    public.get_information()
