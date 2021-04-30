import time

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



start_time = time.clock()
st = 0
# print(f"GCD: {gcd(((13**23547)*(2**1575)*(7**45452)), ((13**147002)*(2**184025)*(7**54057)), st)}")
# print(f"GCD: {gcd(103881042195729914708510518382775401680142036775841, 64202014863723094126901777428873111802307548623680, st)}")
print(f"GCD: {gcd(11111, 1111111, st)}")
duration = time.clock() - start_time
print(f"Duration: {duration}")
