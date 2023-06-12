class Company:
    YEAR = 2023

    def __init__(self, name: str, age: int, count_workers: int, direction: str = 'IT', ):
        self.__name = name
        self.__age = age
        self.__count_workers = count_workers
        self.__direction = direction

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 2:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string of length bigger than 2: {type(new_name)} : {len(new_name)}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and (new_age > 0):
            self.__age = new_age
        else:
            raise TypeError(f'Age should be an int and bigger than 0: {type(new_age)} ; {new_age} <= 0')

    @property
    def count_workers(self):
        return self.__count_workers

    @count_workers.setter
    def count_workers(self, new_count_workers):
        if isinstance(new_count_workers, int) and (new_count_workers > 0):
            self.__count_workers = new_count_workers
        else:
            raise TypeError(f'Count should be an int and bigger than 0: {type(new_count_workers)} ; '
                            f'{new_count_workers} <= 0')

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, new_direction):
        if isinstance(new_direction, str) and len(new_direction) > 1:
            self.__direction = new_direction
        else:
            raise TypeError(f'Direction should be a string of length bigger than 1: {type(new_direction)} : '
                            f'{len(new_direction)}')

    @staticmethod
    def country_homeland():
        print('Our company was founded in Ukraine')

    @classmethod
    def create_company_adding_new_staff(cls, name, age, count_workers, count_new_staff, direction):
        all_company_staff = count_workers + count_new_staff
        return cls(name, age, all_company_staff, direction)

    def company_information(self):
        return f'The name company is {self.__name}. Now, in {self.YEAR}, there are {self.__count_workers} workers.' \
               f'Our company is {self.__age} on market. The direction of company {self.__direction}.'

    def balance_per_one_worker(self, balance: int):
        return f'Balance per one worker: {balance / self.__count_workers}'


if __name__ == '__main__':
    genuisee = Company('Geniusee', 7, 300, 'Technika')
    print(genuisee.name)
    print(genuisee.age)
    print(genuisee.count_workers)
    print(genuisee.direction)
    print(genuisee.company_information())
    print(genuisee.balance_per_one_worker(180000))
    evo = Company('Evo', 7, 300)
    print(evo.direction)
    genuisee.name = 'Gen2'
    print(genuisee.name)
    genuisee.age = 2
    print(genuisee.age)
    genuisee.count_workers = 10
    print(genuisee.count_workers)
    genuisee.direction = 'LOL'
    print(genuisee.direction)

    Company.country_homeland()
    genuisee_with_new_staff = Company.create_company_adding_new_staff("Geniusee", 7, 300, 55, 'IT')
    print(f'With new staff: {genuisee_with_new_staff.count_workers}')
