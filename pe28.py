# 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

total = 0
i = 1
step_size = 2
endpt = 1001 * 1001

while i <= endpt:
    total += i
    print(i)
    if (i ** (1/2)) == int(i ** (1/2)) and i != 1:
        step_size += 2
    i += step_size

print(total)
