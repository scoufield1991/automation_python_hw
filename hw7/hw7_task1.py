import sys


def my_print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    Implement your own print function. It should work on all operating systems.
    You can't use build-in print function.
    """
    output = sep.join(str(obj) for obj in objects) + end
    file.write(output)
    if flush:
        file.flush()


if __name__ == '__main__':
    my_print("Hello", "World", sep=", ", end="!\n", flush=True)
    my_print("Hi")
