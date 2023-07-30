"""
Leetcode 808: Soup Servings https://leetcode.com/problems/soup-servings/.

There are two types of soup: type A and type B. Initially, we have n ml of each
type of soup. There are four kinds of operations:

    Serve 100 ml of soup A and 0 ml of soup B,
    Serve 75 ml of soup A and 25 ml of soup B,
    Serve 50 ml of soup A and 50 ml of soup B, and
    Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it. Each
turn, we will choose from the four operations with an equal probability 0.25.
If the remaining volume of soup is not enough to complete the operation, we
will serve as much as possible. We stop once we no longer have some quantity of
both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used
first.

Return the probability that soup A will be empty first, plus half the
probability that A and B become empty at the same time. Answers within 10^-5 of
the actual answer will be accepted.
"""


import functools


def soup_servings(n: int) -> float:
    """Calculate the probability requested by the problem given input n.

    Args:
        n (int): Quantity of soup in mL.
    Returns:
        Probability that soup A will be empty first plus half the probability
        that A and B become empty at the same time. Returned as a float value.
    """
    if (n >= 4451):  # n asymptotically approaches 1, so simply return 1 if n
        # is large enough for 1 to be within the threshold of acceptance. The
        # threshold can be found by simply running this function and searching
        # for the first output exceeding 0.99999, which is n = 4451.
        return 1
    return 0.25 * (__soup_servings_helper(n - 100, n) +  # Operation 1
                   __soup_servings_helper(n - 75, n - 25) +  # Operation 2
                   __soup_servings_helper(n - 50, n - 50) +  # Operation 3
                   __soup_servings_helper(n - 25, n - 75))  # Operation 4


@functools.cache  # Memoize recursive calls
def __soup_servings_helper(a, b):
    """Recursive helper function for soup_servings(n); should not be called.

    Args:
        a (int): Remaining quantity of soup A in mL.
        b (int): Remaining quantity of soup B in mL.
    Returns:
        Probability that soup A will be empty first plus half the probability
        that A and B become empty at the same time. Returned as a float value.
    """
    if (a <= 0 and b <= 0):
        return 0.5
    elif (a <= 0):
        return 1
    elif (b <= 0):
        return 0
    else:
        return 0.25 * (__soup_servings_helper(a - 100, b) +  # Operation 1
                       __soup_servings_helper(a - 75, b - 25) +  # Operation 2
                       __soup_servings_helper(a - 50, b - 50) +  # Operation 3
                       __soup_servings_helper(a - 25, b - 75))  # Operation 4


# Test cases
print("soup_servings(0):", soup_servings(0))
print("soup_servings(50):", soup_servings(50))
print("soup_servings(100):", soup_servings(100))
print("soup_servings(105):", soup_servings(105))
print("soup_servings(500):", soup_servings(105))
print("soup_servings(4450):", soup_servings(4450))
print("soup_servings(4451):", soup_servings(4451))
print("soup_servings(100000000):", soup_servings(100000000))
