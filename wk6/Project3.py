import time

# 1) implement the modular exponentiation algorithm to compute a^b mod n for any integer inputs a, b and n. Use your
# code to compute a^b mod n for the sets of numbers below. Record the computer run time and iteration count for each.
def getBinExpList(num):
    # function that returns list for all numbers that make binary exponent
    binExpList = []
    binForm = bin(num)[2:]
    for n in range(len(binForm)):
        newExp = int(binForm[len(binForm) - n - 1]) * (2 ** n)
        binExpList.append(newExp)
    return binExpList

def mea(a, b, n):
    start_time = time.time()
    finalNum = 1
    steps = 0
    print(len(getBinExpList(b)))
    for exp in getBinExpList(b):
        finalNum *= (a ** exp) % n
        finalNum = finalNum % n
        if steps % 10 == 0:
            print('hello')
        steps += 1
    duration = time.time() - start_time
    return [finalNum % n, duration, steps]     # [finalNum % n, duration]

def rec_mea(a, b, n):
    if b < 99999999:
        finalNum = 1
        for exp in getBinExpList(b):
            finalNum *= (a ** exp) % n
            finalNum = finalNum % n
        print(finalNum % n)
        return finalNum % n
    else:
        first_half = int(b/2)
        second_half = b - first_half
        return (rec_mea(a, first_half, n) % n) * (rec_mea(a, second_half, n) % n)

def list_mea(a, b, n):
    finalNum = 1
    for exp in getBinExpList(b):
        finalNum *= rec_mea(a, b, n)
        finalNum = finalNum % n
    return finalNum


print(getBinExpList(13530185234470674604))
print(list_mea(9, 105, 137))
# a) a = 2, b = 135301852344706746049, n = 947112966412947222343
# print(rec_mea(2, 13530185234470674604, 947112966412947222343))

# b) a = 13, b = 354224848179261915075, n = 573147844013817084101
# print(mea(13, 354224848179261915075, 573147844013817084101))

# c) a = 3, b = 927372692143078999175, n = 927372692143078999176
# print(mea(3, 927372692143078999175, 927372692143078999176))
