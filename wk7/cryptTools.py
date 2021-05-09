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


print("yeye")
