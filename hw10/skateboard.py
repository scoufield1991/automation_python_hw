from personal_transport import PersonalTransport


class Skateboard(PersonalTransport):
    def __init__(self, speed: float, sync_with_mobile_app: bool):
        super().__init__(seats=0, speed=speed,
                         distance_per_one_charge=10, key=False)
        self._sync_with_mobile_app = sync_with_mobile_app

    def __connect_skateboard_with_mobile(self):
        print('Downloading app from market. ')
        print('Loading app. Sync complete. On next ride you can see information.')

    def information_of_each_ride(self):
        self.start_ride()
        self.finish_ride()
        if self._sync_with_mobile_app is True:
            print(f'Distance per one charge = {self._distance_per_one_charge},your speed = {self._speed}')
        else:
            self.__connect_skateboard_with_mobile()


if __name__ == '__main__':
    skateboard = Skateboard(20, False)
    skateboard.information_of_each_ride()
