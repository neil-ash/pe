# 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# range function: range(start, end, step) w/ start included and end excluded

answer = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        # if statement cuts runtime in half: prevents testing repeats of i and j
        if i <= j:
            check = str(i * j)
            reverse = str(check[len(check) - 1])
            for k in range(len(check) - 2, -1, -1):
                reverse += check[k]
            if reverse == check:
                if int(check) > answer:
                    answer = int(check)

print('\n', answer, '\n')