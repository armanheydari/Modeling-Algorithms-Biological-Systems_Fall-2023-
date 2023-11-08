from Q1 import find_di_pi
from random import shuffle
from math import ceil
from time import time
from tabulate import tabulate


def calculate_lower_bound(pi):
    """
    By finding the breakpoints of the ext(pi) and the [breakpoints/2] formula
    we can find the lower bound
    :list pi: the inputted permutation
    :return: An integer showing the lower bound
    """
    exp_pi = [0] + pi + [len(pi) + 1]
    breakpoints = 0
    for i in range(len(exp_pi) - 1):
        if abs(exp_pi[i + 1] - exp_pi[i]) > 1:
            breakpoints += 1
    return ceil(breakpoints / 2)


if __name__ == '__main__':
    # Generate random permutations
    permutations = [[1], [1, 2], [2, 1]]
    # As n=1 only has 1 and n=2 only has 2 possible random permutations we hard coded them
    for n in range(3, 9):
        identity = [i for i in range(1, n + 1)]
        for i in range(5):
            temp = identity.copy()
            shuffle(temp)
            while temp in permutations:
                shuffle(temp)
            permutations.append(temp)

    # Run the lower bound calculator and smallest distance possible with the brute force algorithm in Q1
    data = [['permutation', 'd(permutation)', 'lower bound', 'execution time']]

    for pi in permutations:
        start = time()  # To calculate the time of the execution
        d_pi = find_di_pi(pi)
        execution_time = time() - start
        lower = calculate_lower_bound(pi)
        data.append([pi, d_pi, lower, execution_time])

    # Generate the table
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    print(table)
