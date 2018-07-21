# 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

for den in range(10, 100):
    for num in range(10, 100):
        if den % 10 != 0:
            if (num / den == int(str(num)[0]) / int(str(den)[0])) or (num / den == int(str(num)[0]) / int(str(den)[1])) or \
               (num / den == int(str(num)[1]) / int(str(den)[0])) or (num / den == int(str(num)[1]) / int(str(den)[1])):
                print(num, den)

