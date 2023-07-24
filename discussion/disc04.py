def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    dp = [0] * (n + 1)  # 创建一个大小为n+1的列表，用于存储路径数

    # 初始化dp[0]
    dp[0] = 1

    # 计算dp[1]到dp[n]的值
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]

    return dp[n]


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[index] * index for index in range(0, len(s)) if index % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1

    n = len(s)
    max_product = [0] * (n + 1)
    max_product[0] = 1
    max_product[1] = s[0]

    for i in range(2, n + 1):
        max_product[i] = max(s[i - 1] * max_product[i - 2], max_product[i - 1])

    return max_product[n]

