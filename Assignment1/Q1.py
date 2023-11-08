from itertools import combinations, product


def reverse_operation(pi, i, j):
    """
    This method does the reverse operation that we need on a list.
    :List pi: The list that we want to do the operation on.
    :Int i: First boundary of the reverse.
    :Int j: Second boundary of the reverse.
    :return: The new list after reversal.
    """
    if j < i:
        i, j = j, i
    temp1 = pi[:i]
    temp2 = pi[i:j+1]
    temp2.reverse()
    temp3 = pi[j+1:]
    return temp1 + temp2 + temp3


def is_rearrange_possible(pi, identity, m, all_combinations):
    """
    This method is the core of the brute force. As we check is it
    possible to rearrange pi with m reverse operations such that
    it turns to the identity.
    :List pi: the inputted permutation.
    :List identity: the identity which is a list from 1 to n.
    :Int m: number of reverse operations.
    :list all_combinations: all possible tuples of reverse gathered in a list.
    :return: a boolean shows is it possible or not.
    """
    # Create every possible sequence of m reverse operations
    m_combinations = list(product(all_combinations, repeat=m))

    # Operate each of the sequences to see if the result is the identity
    for combination in m_combinations:
        temp = pi.copy()

        for i, j in combination:
            temp = reverse_operation(temp, i, j)
        if temp == identity:
            return True

    # If nothing resulted in identity means we need higher m
    return False


def find_di_pi(pi):
    """
    In this function we aimed to find d(pi) with brute force algorithm
    :list pi: The permutation
    :return: an integer which is d(pi)
    """
    # Define the identity that we want to reach out
    identity = [i + 1 for i in range(len(pi))]

    # Try from m=0 to find the least possible number
    all_combinations = list(combinations(list(range(0, len(pi))), 2))
    for m in range(len(pi)):
        if is_rearrange_possible(pi, identity, m, all_combinations):
            return m


if __name__ == '__main__':
    # Get the permutation from the user and store it in a list
    pi = input('please enter the permutation like this 4,2,5,1,3:     ')
    pi = [int(i) for i in pi.split(',')]

    print("d(pi) =", find_di_pi(pi))
