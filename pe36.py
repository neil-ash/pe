# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def binary(num):
    """
    returns binary number as a list when given a number in base 10
    """
    binary_ls = []

    while num > 0:
        binary_ls.insert(0, num % 2)
        num = int(num / 2)

    return binary_ls


total = 0

for i in range(1, 1000000):

    front_i = str(i)
    back_i = ''

    for j in front_i:
        back_i = j + back_i
    
    front_bin = binary(i)
    back_bin = []

    for k in front_bin:
        back_bin.insert(0, k)
    
    if front_i == back_i and front_bin == back_bin:
        #print(front_i, '  ', front_bin)
        total += i

print('\n', total, '\n', sep='')
