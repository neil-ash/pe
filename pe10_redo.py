# 10 redone

#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

##############################################################################################################

# Sieve of Eratosthenes method

# get input (end point)
endpt = int(input('Find all prime numbers up to: '))  # 30

# make list
list = []
for x in range(0, endpt + 1):  # (0, 31)
    list.append(x)

# check list and delete numbers that aren't prime
# for a given divisor (2 -> 7) check all numbers in list
for i in range(2, int(endpt ** 0.5) + 1):  # (2, 8) FIX
    for j in range(2, endpt + 1):  # (2, 31)
        # if number is bigger than divisor and divisible, replace with -1
        if (j > i) and (j % i == 0):
            #print(j, "is divisible by", i)
            list[j] = -1

# make new list with only prime numbers
sum = 0
new_list = []
for k in list:
    # check if list element is != -1 and not 0, 1
    if k > 1:
        new_list.append(k)
        sum += k

# free memory from old list, display new list
del list
print('\n', new_list, '\n', 'Sum is', sum)

