import random


def is_prime(number):
    """
    3. Write a function is_prime that takes 1 argument - a number from 2 to 1000,
    and returns True if it is a prime number, and False otherwise.
    """
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count > 2:
        return False
    elif count == 2:
        return True


if __name__ == '__main__':
    default_number = random.randint(2, 1000)
    print(default_number)
    print(is_prime(default_number))
