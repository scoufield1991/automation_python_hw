from freight_transport import FreightTransport


class Ship(FreightTransport):
    def __init__(self, cargo_compartment: int, type_cargo: str,
                 delivery_rules_for_unexpected_cargo):
        super().__init__(seats=10, speed=30, cargo_compartment=cargo_compartment)
        self._type_cargo = type_cargo
        self._delivery_rules_for_unexpected_cargo = delivery_rules_for_unexpected_cargo

    def __rules_for_unexpected_cargo(self):
        if self._delivery_rules_for_unexpected_cargo is False:
            print('Departments of the company should organize a rally to create rules.')

    def delivery_cargo(self):
        type_cargo_list = ['fuel', 'goods', 'food', 'wood']
        if self._type_cargo.lower() in type_cargo_list:
            self.start_ride()
            self.finish_ride()
        else:
            if self._delivery_rules_for_unexpected_cargo is True:
                print('We can delivery this cargo. ')
                self.start_ride()
                self.finish_ride()
            else:
                print('We can not delivery this cargo. ')
                self.__rules_for_unexpected_cargo()


if __name__ == '__main__':
    ship = Ship(300, 'Water', True)
    ship.delivery_cargo()
