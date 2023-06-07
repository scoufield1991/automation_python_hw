"""
Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
The solution should work and not freeze your computer.
"""


def my_gen():
    for counter in range(0, 10000000001, 2):
        yield counter ** 2


if __name__ == '__main__':
    generator = my_gen()
    for i in my_gen():
        print(i)
