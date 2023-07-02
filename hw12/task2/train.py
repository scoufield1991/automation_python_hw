from hw12.task2.wagon import Wagon


class Train:
    def __init__(self):
        self.wagons = list()

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __repr__(self):
        wagon_numbers = "-".join(str(wagon.number) for wagon in self.wagons)
        return f"<=[HEAD]-{wagon_numbers[::1]}"


if __name__ == '__main__':
    train = Train()
    wagon1 = Wagon(1)
    wagon2 = Wagon(2)
    wagon3 = Wagon(3)
    wagon4 = Wagon(4)

    wagon1.add_passenger("Passenger 1")
    wagon1.add_passenger("Passenger 2")
    wagon2.add_passenger("Passenger 3")

    train.add_wagon(wagon1)
    train.add_wagon(wagon2)
    train.add_wagon(wagon3)
    train.add_wagon(wagon4)

    print(train)
    print(len(wagon1))
    print(len(wagon2))
    print(len(train))
