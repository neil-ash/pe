# 31

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


def find_combos(amount, coin_list):
    """
    takes in an amount and a list of coin values (both in cents)
    """
    # combinations list holds number of possible combinations to make a given amount (amount being list index)
    # first term is 1 (index 0), initialize rest of list as 0s
    combinations = [1]
    for i in range(amount):
        combinations.append(0)

    # iterate thru values of coins in coin_list
    for coin in coin_list:
        # iterate thru indices of elements in combinations
        for i in range(len(combinations)):
            # if the index (aka amount instance) is greater/equal to the value of the coin, then there's a new way to
            # make the combination
            if i >= coin:
                # add max number of combinations to make subamount to number of combinations at an amount instances
                combinations[i] += combinations[i - coin]

    return combinations[amount]


ex_amount = 200
ex_coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
print('\n', find_combos(ex_amount, ex_coin_list), ' combinations!\n', sep='')


