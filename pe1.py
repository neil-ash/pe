# start of Project Euler Problems

# 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Note) solved completely by hand first, got correct answer

def addFact(m, n):
    '''
    :param m: 3 or 5
    :param n: tres or cinco
    :return: factorial form of addition (ex: 1+2+3...n) multiplied by scalar (m)
    '''
    return int(m*((n**2 + n)/2))

# setup
limit = int(1000-1)

tres = int(limit/3)

cinco = int(limit/5)

common = int(limit/(3*5))


#find solution
ans = addFact(3, tres) + addFact(5, cinco) - addFact(3*5, common)

print('\n', ans, '\n')
