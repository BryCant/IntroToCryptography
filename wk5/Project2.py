import time
import string
st = 0

# 1) Use your code to find the greatest common divisor of the pairs of numbers below. Record the computer
# run time and iteration count for each set.
def gcd(big, small, steps):
    # swap inputs if first input less than second
    if small > big:
        temp = small
        small = big
        big = temp

    # find remainder of first input divided by second
    remainder = big % small if small != 0 else 0

    # if second input not equal to 0, compute gcd of second input with remainder
    if small == 0:
        print(f"Steps: {steps}")
        return big
    # if second input equal to zero, return first input
    elif small > 0:
        steps += 1
        return gcd(small, remainder, steps)

# 1a) a = 135301852344706746049, b = 947112966412947222343
start_time = time.clock()
st = 0
print(f"GCD: {gcd(135301852344706746049, 947112966412947222343, st)}")
duration = time.clock() - start_time
print(f"Duration: {duration}")
# Steps: 1
# GCD: 135301852344706746049
# Duration: 9.90999999999631e-05

# 1b) a = 354224848179261915075, b = 573147844013817084101
start_time = time.clock()
st = 0
print(f"GCD: {gcd(354224848179261915075, 573147844013817084101, st)}")
duration = time.clock() - start_time
print(f"Duration: {duration}")
# Steps: 99
# GCD: 1
# Duration: 0.00013449999999998186

# 1c) a = 573147844013817084101, b = 927372692143078999176
start_time = time.clock()
st = 0
print(f"GCD: {gcd(573147844013817084101, 927372692143078999176, st)}")
duration = time.clock() - start_time
print(f"Duration: {duration}")
# Steps: 54
# GCD: 1
# Duration: 7.40000000000185e-05

# --------------------------------------------------------------------------------------------------------------

# 2) Write a program which takes integer inputs a, b and n and then solves the Diophantine equation aX + bY = n or
# indicates that no solution exists.
def dio_solve(a, b, c):
    s_time = time.clock()   # start timing function execution
    print(f"For: {a}(X) + {b}(Y) = {c}")
    # swap inputs if first input less than second
    if b > a:
        temp = b
        b = a
        a = temp

    og_a, og_b = a, b   # for safe keeping ;)
    qs = []     # array to hold quotients
    # if c is not divisible by the gcd, show there's no solution
    cur_gcd = gcd(a, b, st)
    if c % cur_gcd != 0:
        print("No solution exists.")
        return 0
    else:
        # collect quotients until remainder is 0
        while 0 not in qs:
            # collect quotient
            q = divmod(a, b)[0] if b != 0 else 0
            qs.append(q)

            # switch a and b values
            r = a % b if b != 0 else 0
            a = b
            b = r

        # reverse list to ease for loop logic
        print(qs)
        qs.reverse()

        x, y = 0, c/cur_gcd
        for quotient in qs:
            temp_y = y
            y = x - (quotient * temp_y)
            x = temp_y

        dur = time.clock() - s_time
        print(f"Duration: {dur}")
        print(f"X = {x} - {og_a}k; Y = {y} + {og_b}k")
        return [int(x), int(y)]

# 2a) a = 13259581529781261112802, b = 1894225932825894444686, n = 35
print("\n\n\n\n\n\n\n\n")
dio_solve(13259581529781261112802, 1894225932825894444686, 35)

# 2b) a = 354224848179261915075, b = 573147844013817084101, n = 5
dio_solve(354224848179261915075, 573147844013817084101, 5)

# 2c) a = 573147844013817084101, b = 927372692143078999176, n = 21
dio_solve(573147844013817084101, 927372692143078999176, 21)

''' #2 Output
For: 13259581529781261112802(X) + 1894225932825894444686(Y) = 35
Steps: 1
No solution exists.
For: 354224848179261915075(X) + 573147844013817084101(Y) = 5
Steps: 99
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0]
Duration: 0.0003155000000000102
X = -6.765092617235338e+20 - 573147844013817084101k; Y = 1.094614979172776e+21 + 354224848179261915075k
For: 573147844013817084101(X) + 927372692143078999176(Y) = 21
Steps: 54
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 22, 2, 3, 2, 2, 1, 1, 1, 2, 25, 5, 19, 4, 2, 1, 1, 1, 1, 1, 3, 4, 3, 2, 9, 2, 1, 13, 8, 1, 8, 0]
Duration: 0.00015959999999999586
X = 1.353925409674378e+21 - 927372692143078999176k; Y = -2.1906973309671564e+21 + 573147844013817084101k
'''

# --------------------------------------------------------------------------------------------------------------

# 3) Write a program in Python that
#  a) Prompts the user to encrypt or decrypt;
e_or_d = input("\nDo you want to encrypt or decrypt? ")

#  b) prompts the user for a lowercase message;
message = input("What is your message? ").lower()

#  c) prompts the user for a multiplicative key;
m_key = int(input("Enter multiplicative key: ")) % 26

#  d) performs the multiplicative encryption to each letter modulo 26;
new_message = ""
if e_or_d == 'e':
    for letter in message:
        new_letter = chr((((ord(letter) - 96) * m_key) % 26) + 96)
        new_message += new_letter if letter in string.ascii_lowercase else letter
elif e_or_d == 'd':
    for letter in message:
        new_letter = chr((dio_solve(m_key, 26, (ord(letter) - 96))[1] % 26) + 96)
        new_message += new_letter if letter in string.ascii_lowercase else letter

#  e) prints the encrypted/decrypted message.
print(f"\nFinal message: {new_message}")

# --------------------------------------------------------------------------------

# 4) see paper

# 5)
# a) Find the multiplicative inverse of 37 modulo 27989898
dio_solve(37, 27989898, 1)
# X = -8321321

# b) Decrypt the following ciphertext message, which was encrypted by  converting a plaintext
# message into four-letter blocks,  and performing multiplication by 37modulo 27989898.
# Strategy: (4BLOCK_NUMBER * -8321321)  mod 27989898
# Result: 16-01-02-12 15-27-16-09 03-01-19-19 15-27-27-27
#    p-a-b-l  o-#-p-i  c-a-s-s  o-#-#-#  ---> pablo picasso
