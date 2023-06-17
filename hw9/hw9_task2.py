class Worker:
    CITIZENSHIP = 'Ukraine'

    def __init__(self, name: str, surname: str, age: int, education: bool, level: str, salary: float,
                 experience: int, gender: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__education = education
        self.__level = level
        self.__salary = salary
        self.__experience = experience
        self.__gender = gender

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
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if isinstance(new_surname, str) and len(new_surname) > 2:
            self.__name = new_surname
        else:
            raise TypeError(f'Surname should be a string of length bigger than 2: {type(new_surname)} : '
                            f'{len(new_surname)}')

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
    def education(self):
        return self.__education

    @education.setter
    def education(self, new_education):
        if isinstance(new_education, bool):
            self.__name = new_education
        else:
            raise TypeError(f'Education should be boolean: {type(new_education)}.')

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level):
        levels = ['junior', 'middle', 'senior']
        if isinstance(new_level, str) and (new_level.lower() in levels):
            self.__level = new_level
        else:
            raise TypeError(f'Level should be a string: {type(new_level)} , '
                            f'and consist of like junior, middle or senior')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, float) and (new_salary > 0):
            self.__salary = new_salary
        else:
            raise TypeError(f'Salary should be a float and bigger than 0: {type(new_salary)} ; {new_salary} <= 0')

    @property
    def experience(self):
        return self.__experience

    @age.setter
    def experience(self, new_experience):
        if isinstance(new_experience, int) and (new_experience > 0):
            self.__salary = new_experience
        else:
            raise TypeError(f'Salary should be an int and bigger than 0: {type(new_experience)} ; '
                            f'{new_experience} <= 0')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        gender_list = ['female', 'male']
        if isinstance(new_gender, str) and (new_gender.lower() in gender_list):
            self.__level = new_gender
        else:
            raise TypeError(f'Level should be a string: {type(new_gender)} , '
                            f'and consist of like female or male')

    def worker_information(self):
        female_template = f'Our worker name is {self.__name}, surname - {self.__surname}. ' \
                          f'She is from {self.CITIZENSHIP}. ' \
                          f'She worked in out company for {self.__experience} years. ' \
                          f'Her salary is {self.__salary}. ' \
                          f'She is {self.__age} years old. '
        male_template = f'Our worker name is {self.__name}, surname - {self.__surname}. ' \
                        f'He is from {self.CITIZENSHIP}. ' \
                        f'He worked in out company for {self.__experience} years. ' \
                        f'His salary is {self.__salary}. ' \
                        f'He is {self.__age} years old. '
        if (self.__gender.lower() == 'female') and (self.__education is True):
            return female_template + 'She finished university.'
        elif (self.__gender.lower() == 'female') and (self.__education is False):
            return female_template + 'She finished only school.'
        elif (self.__gender.lower() == 'male') and (self.__education is False):
            return male_template + 'He finished only school.'
        elif (self.__gender.lower() == 'male') and (self.__education is True):
            return male_template + 'He finished only university.'

    @staticmethod
    def worker_direction():
        print('Our worker worked in IT direction.')

    @classmethod
    def worker_bonus(cls, name, surname, age, education, level, salary, bonus, experience, gender):
        salary_with_bonus = salary + bonus
        return cls(name, surname, age, education, level, salary_with_bonus,
                   experience, gender)


if __name__ == '__main__':
    yurii = Worker('Yurii', 'Kondrashev', 28, True, 'Junior', 15700, 2, 'Male')
    print(yurii.name)
    print(yurii.worker_information())
    # yurii.level = 'Senior1'
    yurii.level = 'Senior'
    print(yurii.level)

    tomas = Worker.worker_bonus('Tomas', 'Bailey', 1, True, 'Senior', 25550.85, 511.99, 5, 'male')
    print(tomas.salary)
