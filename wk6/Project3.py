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
    def innards(k):
        if k >= len(bin(b)[2:]):
            return 1
        else:
            # print(int(bin(b)[::-1][k]))
            if int(bin(b)[::-1][k]) == 1:
                fin = a
                for i in range(k):
                    fin = (fin ** 2) % n
                print(f"K = {k}; {int(bin(b)[::-1][k])} * {fin} * innards({k + 1})")
                return fin * innards(k + 1)
            else:
                print(f"K = {k}; {int(bin(b)[::-1][k])} * {((a ** k) % n)} * innards({k + 1})")
                return innards(k + 1) % n
    return innards(0) % n




def list_mea(a, b, n):
    finalNum = 1
    for exp in getBinExpList(b):
        finalNum *= rec_mea(a, b, n)
        finalNum = finalNum % n
    return finalNum


# print(getBinExpList(13530185234470674604))
print(getBinExpList(105))
# print(rec_mea(9, 105, 137))
# a) a = 2, b = 135301852344706746049, n = 947112966412947222343
print(rec_mea(2, 13530185234470674604, 947112966412947222343))

# b) a = 13, b = 354224848179261915075, n = 573147844013817084101
# print(mea(13, 354224848179261915075, 573147844013817084101))

# c) a = 3, b = 927372692143078999175, n = 927372692143078999176
# print(mea(3, 927372692143078999175, 927372692143078999176))
