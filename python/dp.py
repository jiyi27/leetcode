from typing import List

"""
Fibonacci numbers
"""


def fibRecursive(n: int) -> int:
    if n < 2:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)


def fibDp(n: int) -> int:
    if n < 2:
        return n
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]


"""
Climbing stairs
"""


def climbStairs(n: int) -> int:
    if n < 2:
        return n
    arr = [0] * (n+1)
    arr[0] = 1
    arr[1] = 2

    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n - 1]


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)  # dp[i]表示到达位置i的最小成本

    # 可以从位置0或位置1开始，所以这两个位置的成本都是0
    dp[0] = dp[1] = 0

    # 到达位置i的最小成本 = 到达前面某个位置的最小成本 + 那个位置的cost值
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    return dp[n]
