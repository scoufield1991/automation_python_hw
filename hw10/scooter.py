from personal_transport import PersonalTransport


class Scooter(PersonalTransport):
    def __init__(self, speed: float, key: bool, beep: bool, information_panel: bool):
        super().__init__(seats=0, speed=speed,
                         distance_per_one_charge=40, key=key)
        self._beep = beep
        self._information_panel = information_panel

    def __check_information_panel(self):
        print(f'Distance per one charge = {self._distance_per_one_charge}, speed = {self._speed}')

    def daily_ride(self):
        self.start_ride()
        self.__check_information_panel()
        self.finish_ride()


if __name__ == '__main__':
    scooter = Scooter(30, True, True, True)
    scooter.daily_ride()
