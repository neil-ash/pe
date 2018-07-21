# 3

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# NEED FUNCTION DEFINITION BEFORE FUNCTION CALL IN PYTHON
def isPrime(n):
    for j in range(2, int(n/2)):  # don't need int(i/2 + 1) since checking if i is prime
        if n % j == 0:
            return False
    else:
        return True


x = int(input("Enter number: "))

for i in range(2, int(x/2 + 1)):  # need to check all possible factors of x
    if x % i == 0:  # if i is a factor of x, check if i is prime
        if isPrime(i):
            lpf = i

print(lpf)
