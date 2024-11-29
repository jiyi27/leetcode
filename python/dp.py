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


"""
62 Unique Path
"""


def uniquePathsRecursive(self, m: int, n: int) -> int:
    def dfs(down: int, right: int) -> int:
        # 必须检查, 不然会一直往下或者往右运动, 不会停止
        if down > m or right > n:
            return 0
        if down == m and right == n:
            return 1
        return dfs(down+1, right) + dfs(down, right+1)
    return dfs(1, 1)


def uniquePaths(self, m: int, n: int) -> int:
    # 如果 n = 3，那么 [0] * 3 会得到 [0, 0, 0]
    # for _ in range(m) 表示这个操作要重复 m 次
    dp = [[0] * n for _ in range(m)]

    # 设置第一行和第一列的基本情况
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # 计算每个单元格的唯一路径数
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 返回右下角单元格的唯一路径数
    return dp[m - 1][n - 1]
