from personal_transport import PersonalTransport


class Car(PersonalTransport):
    def __init__(self, speed: float, key: bool, brand: str, color: str):
        super().__init__(seats=2, speed=speed,
                         distance_per_one_charge=100, key=key)
        self._brand = brand
        self._color = color

    def __can_rich_distance(self):
        normal_speed = 50
        normal_expense_charging_per_kilometer = self._distance_per_one_charge / normal_speed
        expense_charging_per_kilometer = self._distance_per_one_charge / self._speed
        if expense_charging_per_kilometer < normal_expense_charging_per_kilometer:
            print(f'You can not rich this distance: {self._distance_per_one_charge} kilometers. '
                  f'You need to find charging!!!')
        else:
            print(f'You can rich this distance: {self._distance_per_one_charge} kilometers')

    def car_information(self):
        print(f'My car - {self._brand}, color {self._color}, speed {self._speed}.')

    def car_ride(self):
        self.start_ride()
        self.__can_rich_distance()
        self.finish_ride()


if __name__ == '__main__':
    car = Car(55, True, 'Tesla', 'Black')
    car.car_ride()
    car.car_information()
