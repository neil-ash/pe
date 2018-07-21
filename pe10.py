# 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


# more efficient function to check if a number is prime
def is_prime(m):
    """
    :param m: number to check
    :return: number if it is prime, returns 0 if not prime
    """
    for i in range(2, int((m**0.5) + 1)):
        if m % i == 0:
            return 0
    # else will work if loop completes OR if loop does not run at all
    else:
        return m


# efficient way to do it
sum = 2 + 3
n = 1

# while 6*n - 1 < 10 and 6*n + 1 < 10:
max = 2000000
while True:
    if is_prime(6*n - 1) <= max:
        sum += is_prime(6*n - 1)
    else:
        break

    if is_prime(6*n + 1) <= max:
        sum += is_prime(6*n + 1)
    else:
        break

    n += 1

print('\n', sum)

