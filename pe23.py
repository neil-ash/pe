# 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
# sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def check_abundance(num):
    """
    returns True if input is abundant number, False if otherwise
    """
    div_list = []
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            div_list.append(i)
            if i != num / i and i != 1:
                div_list.append(int(num/i))

    if sum(div_list) > num:
        return True
    else:
        return False


def add_fact(n):
    """
    returns the sum of all numbers up to and including input
    """
    total = 0
    for i in range(n + 1):
        total += i

    return total


# first, make list of all abundant numbers
abundant_list = []
for i in range(12, 28123):
    if check_abundance(i):
        abundant_list.append(i)

# then, find sum of all numbers 1 -> 28123
added_sum = add_fact(28123)

# find all unique combinations of 2 elements in list
import itertools
sum_of_abundants = set()
for i in (itertools.combinations(abundant_list, 2)):
    if sum(i) <= 28123:
        sum_of_abundants.add(sum(i))

# need to account for (abudant_number + itself) -- not accounted for in itertools.combinations
for i in abundant_list:
    if 2 * i <= 28123:
        sum_of_abundants.add(2 * i)

# answer: (sum of all numbers from 1 -> 28123) - (sum of all numbers that can be written as sum of 2 abundant numbers)
print(added_sum - sum(sum_of_abundants))

