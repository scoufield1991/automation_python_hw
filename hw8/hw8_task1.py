"""
Create a decorator that prints to the console the name of the function that was called.
The function should work as intended.
For example, create a pair of functions for the arithmetic operations of summation and multiplication.
When calling these functions, the result of the operation must be returned and the name of the function
that was called must be displayed in the console with the result.
"""


def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@print_function_name
def summation(num_1, num_2):
    return num_1 + num_2


@print_function_name
def multiplication(num_1, num_2):
    return num_1 * num_2


if __name__ == '__main__':
    result_sum = summation(3, 4)
    print("Result:", result_sum)
    result_mul = multiplication(2, 5)
    print("Result:", result_mul)
