# Davis Sandefur
# Completed 20/4/15

# Part A: Catalan numbers with recursion


def catalan(n):
    """
    :param n: Whole number of whichever Catalan number you want to find (such as C10)
    :return: Cn
    """
    if n == 0:
        return 1

    else:
        return ((4*n-2)/(n+1))*catalan(n-1)

# Part B, Euclid gcd


def euclid(m, n):
    """
    :param m: One whole number
    :param n: The other whole number
    :return: The greatest common divisor of n and m
    """

    if n == 0:
        return m

    else:
        return euclid(n, m % n)


if __name__ == "__main__":
    print(catalan(1))
    print(catalan(2))
    print(catalan(0))
    print(euclid(3, 6))