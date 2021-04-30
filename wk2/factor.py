'''
Write a function that takes an integer as an input, and returns a list of all positive factors for the input
'''
user_num = int(input("Enter a positive integer: "))


def get_factors(x):
    factors = []
    for num in range(1, x + 1):
        if x % num == 0:
            factors.append(num)

    return factors


print(get_factors(user_num))

'''
Problem 2: An integer is called "perfect" if it is equal to the sum of its proper factors, ie, factors that are 
less than the integer itself. Write a program that finds the perfect numbers less than one thousand.
'''
perfect_nums = []
for n in range(1, 1000):
    if n == sum(get_factors(n)[:len(get_factors(n)) - 1]):
        perfect_nums.append(n)
        print(get_factors(n))

print(perfect_nums)
