# 24

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
def pe24(endpt):
    """

    """
    idx = 0

    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        for f in range(0, 10):
                            for g in range(0, 10):
                                for h in range(0, 10):
                                    for i in range(0, 10):
                                        for j in range(0, 10):
                                            if len(set([a, b, c, d, e, f, g, h, i, j])) == 10:
                                                idx += 1
                                            if idx == endpt:
                                                return a, b, c, d, e, f, g, h, i, j


print(pe24(5))
'''

idx = 0

for i in range(0, 9999999999):
    s = str(i)
    if len(set(s)) == 10:
        print(i)
        idx += 1
    if idx == 1000000:
        print(i)
        break

