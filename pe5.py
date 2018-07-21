# 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_prime(n):
    """
    :param n: number to check
    :return: returns n if n is prime, returns 'None' if n is not prime
    """
    for j in range(2, int(n/2) + 1):  # don't need int(i/2 + 1) since checking if i is prime
        if n % j == 0:
            return
    else:
        return n


list = []
for i in range(2,21):
    list.append(is_prime(i))


factors = []
total = 1
for j in list:
    if isinstance(j, int):
        k = 1
        original_j = j
        while original_j**k <= 20:
            j = original_j**k
            k += 1
        factors.append(j)
        total *= j

print(list)
print(factors)
print(total)



