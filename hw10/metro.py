from public_transport import PublicTransport


class Metro(PublicTransport):
    def __init__(self, event_with_musicians: bool, charity_event: bool):
        super().__init__(seats=90, speed=55, conductor_availability=False, ticket_cost=9.40,
                         start_station='Pochaina', end_station='Libidska')
        self._event_with_musicians = event_with_musicians
        self._charity_event = charity_event

    def __charity_in_metro(self):
        if self._charity_event is True:
            print('Group of people collect money for helping our army. I give them some money.')
        else:
            print('I am standing in metro carriage and waiting my station. ')

    def __event_with_musicians_in_metro(self):
        if self._event_with_musicians is True:
            print('Group of people collect sing Ukranian national song. I give them some money.')
        else:
            print('I still standing in metro carriage and waiting my station. ')

    def ride_in_metro(self):
        self.start_ride()
        self.__charity_in_metro()
        self.__event_with_musicians_in_metro()
        self.finish_ride()


if __name__ == '__main__':
    metro = Metro(True, True)
    metro.ride_in_metro()
