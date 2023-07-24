# def wears_jacket_with_if(temp, raining):
#     """
#     >>> wears_jacket_with_if(90, False)
#     False
#     >>> wears_jacket_with_if(40, False)
#     True
#     >>> wears_jacket_with_if(100, True)
#     True
#     """
#     return temp < 60 or raining

# def square(x):
#     print("here!")
#     return x * x
#
# def so_slow(num):
#     x = num
#     while x > 0:
#         x = x + 1
#     return x / 0
#
# square(so_slow(5))

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    k = 2
    result = False
    while n % k != 0:
        k = k + 1
        if k == n:
            result = True

    return result



