# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def find_div(num):
    div_list = []
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            div_list.append(i)
            if i != num / i and i != 1:
                div_list.append(int(num/i))

    return div_list


final_list = []

for i in range(1, 10001):
    if i == sum(find_div(sum(find_div(i)))) and i != sum(find_div(i)):
        if i not in final_list:
            final_list.append(i)
            final_list.append(sum(find_div(i)))

print(sum(final_list))
