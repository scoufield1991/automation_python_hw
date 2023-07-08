class Scooter:
    def __init__(self, speed: int) -> None:
        self.__mark = "Kugoo"
        self.__speed = speed

    def __repr__(self):
        return "I am from repr"

    def __str__(self):
        return (
            f'{self.__class__.__name__}:\n{{\n\t"speed": {self.__speed}\n\t"mark": {self.__mark}\n}}'
        )


if __name__ == '__main__':
    kugoo = Scooter(25)
    print(kugoo)
