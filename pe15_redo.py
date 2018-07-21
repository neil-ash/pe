# 15 redone

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

# question rephrased: how many different combinations of 20 units can fill 40 spots?
# answer: 40 choose 20

########################################################################################################################

# simple method using equation of n!/k!(n-k)! with n = 40, k = 20

from math import factorial as fact

print(int(fact(40) / (fact(20) * fact(40 - 20))))

########################################################################################################################

# outputting pascal's triangle, max of a given row gives result of above equation

n = 41  # needed to get answer: 2^40, need middle term so 41 since odd

new_list = []
for i in range(1, n + 1):
    old_list = new_list
    new_list = []

    for _ in range(i):
        new_list.append(0)

    new_list[0] = new_list[i - 1] = 1

    for j in range(1, i - 1):
        new_list[j] = old_list[j - 1] + old_list[j]

    print(new_list)

print(max(new_list))



