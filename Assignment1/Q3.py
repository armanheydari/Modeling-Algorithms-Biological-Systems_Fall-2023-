from Q1 import find_di_pi, reverse_operation
from Q2 import calculate_lower_bound


def find_breakpoints(pi):
    """
    Find all the breakpoints of a permutation.
    :list pi: the inputted permutation
    :return: a list of integers showing the indexes of breakpoints
    """
    breakpoints = []
    for i in range(len(pi) - 1):
        if abs(pi[i + 1] - pi[i]) > 1:
            breakpoints.append(i + 1)
    return breakpoints


def is_descending(lst):
    """
    To find out a list is descending or not
    :param lst: any list
    :return: a boolean that is true only when the inputted list is ascending
    """
    if len(lst) == 1:
        return False
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            return False
    return True


def calculate_upper_bound(pi):
    """
    Find the upper bound of d(permutation) using breakpoints and strips
    :list pi: the inputted permutation
    :return: An integer showing the upper bound
    """
    exp_pi = [0] + pi + [len(pi) + 1]
    result = 0
    breakpoints = find_breakpoints(exp_pi)
    # We should continue the algorithm until we reach the identity which doesn't have any breakpoints
    while len(breakpoints) > 0:
        i = 0
        # Generate the strips using the breakpoints that we have
        strips = [exp_pi[:breakpoints[0]]]
        for j in range(1, len(breakpoints)):
            strips.append(exp_pi[breakpoints[i]:breakpoints[j]])
            i = j
        strips.append(exp_pi[breakpoints[-1]:])
        # Find the minimum number between all descending strips
        min_descending = len(exp_pi) + 1
        for i, s in enumerate(strips):
            if (len(s) == 1 and 0 < i < len(strips) - 1) or is_descending(s):
                if min_descending > s[-1]:
                    min_descending = s[-1]
        # Where there was a descending strip
        if min_descending < len(exp_pi) + 1:
            index2 = exp_pi.index(min_descending)
            index1 = exp_pi.index(min_descending-1)
            if index2 < index1:
                index2, index1 = index1, index2
            # Reverse from that minimum until the index of -1 of that
            exp_pi = reverse_operation(exp_pi, index1+1, index2)
        # In case of there are no descending strip
        else:
            for s in strips:
                if len(s) > 1:
                    # just reverse an ascending strip to create a descending one
                    index2 = exp_pi.index(s[-1])
                    index1 = exp_pi.index(s[0])
                    exp_pi = reverse_operation(exp_pi, index1, index2)
                    break
        # Count the number of reverses
        result += 1
        breakpoints = find_breakpoints(exp_pi)

    return result


if __name__ == '__main__':
    pi = [4, 3, 6, 5, 1, 8, 7, 2]
    print("Lower bound =", calculate_lower_bound(pi))
    print("Higher bound =", calculate_upper_bound(pi))
    print("The exact d(pi)=", find_di_pi(pi))
