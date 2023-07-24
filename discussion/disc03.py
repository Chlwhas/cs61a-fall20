def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    # base case
    if n == 1:
        return m
    # recursive case
    else:
        return m + multiply(m, n - 1)


def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1


print(rec(3, 2))


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    # iteration
    k = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        k += 1
        print(n)
    return k

    # recursion
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)


def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 % 10 <= n2 % 10:
        return n1 % 10 + 10 * merge(n1 // 10, n2)
    else:
        return n2 % 10 + 10 * merge(n1, n2 // 10)


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n - 1))
    return repeat


def is_prime_iteration(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def is_prime_recursion(n):
    """
    >>> is_prime_recursion(7)
    True
    >>> is_prime_recursion(10)
    False
    >>> is_prime_recursion(1)
    False
    """
    def prime_helper(k):
        if k == n:
            return True
        elif n == 1 or k < n and n % k == 0:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper(2)









