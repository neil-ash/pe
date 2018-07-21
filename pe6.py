# 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# easy way

sum_of_squares = 0
base = 0

for i in range(101):
    base += i
    sum_of_squares += i**2

square_of_sums = base**2

print(square_of_sums - sum_of_squares)
'''


# harder/more interesting way

def recur(m):
    if m <= 0:
        return 0
    else:
        return recur(m-1) + m**2


x = 100
base = int(x * (x + 1) / 2)
square_of_sums = base**2
sum_of_squares = recur(x)
print(square_of_sums - sum_of_squares)
