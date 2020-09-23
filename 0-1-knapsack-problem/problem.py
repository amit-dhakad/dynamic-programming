# code

""" You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it(0-1 property). """


def knapSackRecursive(val, weight, c, n):

    # base condition
    if n == 0 or c == 0:
        return 0

    if weight[n-1] > c:
        return knapSackRecursive(val, weight, c, n-1)

    else:
        return max(val[n-1] + knapSackRecursive(val, weight, c - weight[n-1], n-1), knapSackRecursive(val, weight, c, n-1))


def knapSackMemoization(val, weight, c, n):

    # base condition
    if n == 0 or c == 0:
        return 0

    if t[n][c] != -1:
        return t[n][c]

    if weight[n-1] > c:
        t[n][c] = knapSackMemoization(val, weight, c, n-1)
        return t[n][c]
    else:
        t[n][c] = max(val[n-1] + knapSackMemoization(val, weight, c -
                                                     weight[n-1], n-1), knapSackMemoization(val, weight, c, n-1))
        return t[n][c]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

# We initialize the matrix with -1 at first.
# This is require for memoization
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print('recursive', knapSackRecursive(val, wt, W, n))
print('\n')
print('memoization', knapSackMemoization(val, wt, W, n))
