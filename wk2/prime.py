import math


def get_factors(x):
    factors = []
    for n in range(1, math.floor(math.sqrt(x))):
        if x % n == 0:
            factors.append(n)
            factors.append(x/n)

    return sorted(factors)


'''
# Method too slow
def is_prime(x):
    if len(get_factors(x)) <= 2:
        return True
    else:
        return False
'''


def new_is_prime(n):
    isPrime = True
    for x in range(2, math.floor(math.sqrt(n))):
        if (n % x) == 0:
            isPrime = False
            break
    return isPrime if n > 2 else False

print(get_factors(221))
'''
Program 2: The Fibonacci numbers are a sequence of numbers 0,1,1,2,3,5,... 
It is defined recursively as F_n=F_(n-1)+F_(n-2). Write a program that outputs 
the nth Fibonacci number for any positive integer n
'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


num = 1
for i in range(49, 52):
    print(fib(i)/num)
    num = fib(i)

