# 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?

# COME BACK TO, CONSIDER FACT THAT EVERY PRIME NUMBER CAN BE WRITTEN AS (6n +/- 1)


def is_prime(n):
    """
    :param n: number to check
    :return: returns True (yes prime) or False (not prime)
    """
    for j in range(2, int(n/2) + 1):
        if n % j == 0:
            return False
    else:
        return True


i = j = 0
while i <= 10001:
    j += 1
    if is_prime(j):
        i += 1

print(j)



