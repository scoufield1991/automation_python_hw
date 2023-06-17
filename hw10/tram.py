from public_transport import PublicTransport


class Tram(PublicTransport):
    def __init__(self, conductor_availability: bool, start_station: str, end_station: str, route_number: int):
        super().__init__(seats=40, speed=45, conductor_availability=conductor_availability, ticket_cost=8.50,
                         start_station=start_station, end_station=end_station)
        self._route_number = route_number

    def __information_in_tram(self):
        print('From 1 till 10 this month you can buy travel card')

    def check_tram(self):
        route_number_list = [1, 3, 5]
        if self._route_number in route_number_list:
            print(f'This route {self._route_number} is correct for my way.')
            self.start_ride()
            self.__information_in_tram()
            self.finish_ride()
        else:
            print('This route is not correct for my way. I will wait next tram.')


if __name__ == '__main__':
    tram = Tram(False, 'Balzak street', 'Mikitenko street', 3)
    tram.check_tram()
