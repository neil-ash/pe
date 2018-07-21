# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

"""
# dumb method

x = 2 ** 1000
x = str(x)

total = 0
for i in x:
    total += int(i)

print(total)
"""

# smarter/more interesting method (same algorithm would work in C++ where int range is smaller)


def two_power(n):
    """
    :param n: power of 2
    :return: list with elements composing resultant power of 2
    """
    ls = [1]

    for i in range(n):
        # multiply each element in list by 2
        ls = [j * 2 for j in ls]
        # check if mutliplication results in any elements greater than 10, if so, do % and carry
        for k in range(len(ls)):
            if ls[k] >= 10:
                ls[k] = ls[k] % 10
                if k - 1 < 0:
                    ls.insert(0, 1)
                else:
                    ls[k - 1] += 1
        # fix issue: last entry was 2 digits
        for l in range(len(ls)):
            if ls[l] >= 10:
                ls[l] = ls[l] % 10
                if l - 1 < 0:
                    ls.insert(0, 1)
                else:
                    ls[l - 1] += 1

    return ls


print(sum(two_power(1000)))
