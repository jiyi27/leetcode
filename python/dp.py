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
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n - 1]


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)  # 到达第i台阶所花费的最少体力为dp[i]

    # 可以从位置0或位置1开始，所以这两个位置的成本都是0
    dp[0] = dp[1] = 0

    # dp[i - 1] 跳到 dp[i] 需要花费 dp[i - 1] + cost[i - 1]
    # dp[i - 2] 跳到 dp[i] 需要花费 dp[i - 2] + cost[i - 2]
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    return dp[n]
