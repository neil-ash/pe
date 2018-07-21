# 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def simple_py_trip():
    """
    Inefficient solution
    """
    for c in range(1,1000):
        for b in range(1,1000):
            if b < c:
                for a in range(1,1000):
                    if a < b:
                        if a**2 + b**2 == c**2 and a + b + c == 1000:
                            print("a,b, and c are:", a, b, c)
                            print("a, b, and c squared are:", a**2, b**2, c**2)
                            print("Their product is:", a*b*c)
                            return


def better_py_trip():
    """
    Rewrite c as (1000 - a - b), only 2 loops needed instead of 3
    """
    for a in range(1, 1000):
        # since b is inner loop, ensures a < b
        for b in range(1, 1000):
            # since c = (1000 - a - b) is on right side of equality, ensures b < c (thus a < b < c)
            if a**2 + b**2 == (1000 - a - b)**2:
                    print(a * b * (1000 - a - b))
                    print(a, b, (1000 - a - b))
                    # since function returns when answer is found, no need for if statements checking a < b < c
                    return


better_py_trip()

