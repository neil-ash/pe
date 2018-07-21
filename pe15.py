# 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

import random

dimen = 4

full = ['q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q']
reps = 0
unique = 0

while reps < 10000:

    temp = []
    right = down = 0

    while right <= dimen and down <= dimen:

        if right + down == 2 * dimen:
            break

        if right == dimen:
            down += 1
            temp.append('d')

        elif down == dimen:
            right += 1
            temp.append('r')

        else:
            if random.choice([True, False]):
                right += 1
                temp.append('r')
            else:
                down += 1
                temp.append('d')

    a = full
    b = temp
    # to see if all the elements in b exist within a in the same order
    if any(a[i:i + len(b)] == b for i in range(len(a) - len(b) + 1)):
        pass
    else:
        unique += 1
        full.append('x')
        for i in temp:
            full.append(i)
            print(i, end='')
        print('\n')

    reps += 1

print('For a grid with dimensions', dimen, 'x', dimen, 'there are', unique, 'unique paths!\n')
