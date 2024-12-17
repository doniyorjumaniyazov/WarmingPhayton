import time
from typing import Callable

def main(func):
    def wrapper(*args, **kwargs):
        print(f'zapusk {func.__name__} v {time.time()}')
        result = func(*args, **kwargs)
        print(f'dalee {func.__name__}: {result}')
        print(f'zaversheunya {func.__name__} v {time.time()}')
        return result
    return wrapper
@main
# def factorial(n: int):
#     f = 1
#     for i in range(2, n+1):
#         f *= i
#     return f
def fib(n: int):
    sum = 0
    if n == 1:
        return 1
    elif n < 0:
        return 0
    elif n > 1:
        return (n-2) + (n-1)
        
    

print(fib(10))
#print(factorial(50))
# control = main(factorial)
# print(f'{control.__name__ = } ')
# print(f'{control(800) = }')
    