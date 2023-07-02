class Wagon:
    def __init__(self, number: int):
        self.number = number
        self.passengers = list()

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("Wagon is already full. Cannot add more passengers.")

    def __len__(self):
        return len(self.passengers)

    def __repr__(self):
        return f"[{self.number}]"
