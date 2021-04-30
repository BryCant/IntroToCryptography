import math


# 1) pi(100000)
def new_is_prime(n):
    isPrime = True
    for x in range(2, math.floor(math.sqrt(n)) + 2):
        if (n % x) == 0 and n != 2:
            isPrime = False
            break
    return isPrime if n >= 2 else False


def count_prime(r):
    prime_counter = 0
    for i in range(1, r):
        if new_is_prime(i):
            # print(f"Val: {i}, Prime: {new_is_prime(i)}")   // for troubleshooting
            prime_counter += 1
    return prime_counter


print("here ", count_prime(1000000000))
# -----------------------------------------------------------------------------

# 2) Demonstrate the Prime Number Theorem
for n in range(2, 99999999, 50000):
    print(f"n = {n}: {count_prime(n)/(n/math.log(n))}")

'''
OUTPUT:
n = 50002: 1.110718116270783
n = 100002: 1.1042996429879008
n = 150002: 1.1003718330333263
n = 200002: 1.0975599758818184
n = 250002: 1.0959505051740874
n = 300002: 1.092867115199537
n = 350002: 1.0933572192920373
n = 400002: 1.0919139219578606
n = 450002: 1.090733584504446
n = 500002: 1.0901494316468507
n = 550002: 1.089180704373409
'''

# 3) See attachment

# 4) Golden Ratio
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


num = 1
for i in range(1, 30):
    print(fib(i)/num)
    num = fib(i)

# 5) See attachment
# 6) See attachment
