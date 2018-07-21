# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
'''
n = 4

ls = [1]

for i in range(1, n + 1):
    # multiply each element in list by i (goes from 1 -> n)
    ls = [j * i for j in ls]
    # check if mutliplication results in any elements greater than 10, if so, do % and carry
    for k in range(len(ls)):
        if ls[k] >= 10:
            old = ls[k]
            ls[k] = ls[k] % 10
            if k - 1 < 0:
                ls.insert(0, (old - ls[k]) % 10)
            else:
                ls[k - 1] += ls[k]

    """
    # fix issue: last entry was 2 digits
    for l in range(len(ls)):
        if ls[l] >= 10:
            ls[l] = ls[l] % 10
            if l - 1 < 0:
                ls.insert(0, 1)
            else:
                ls[l - 1] += 1
    """

print(ls)
'''

# easy way

x = 1
ls = []

for i in range(1, 101):
    x *= i

x = str(x)

total = 0
for i in x:
    total += int(i)

print(total)
