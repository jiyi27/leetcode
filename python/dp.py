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
    # 如果 n = 3，那么 [0] * 3 会得到 [0, 0, 0] - 1. 声明数组
    # for _ in range(m) 表示这个操作要重复 m 次
    dp = [[0] * n for _ in range(m)]

    # 设置第一行和第一列的基本情况 - 2. 设置初始状态
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # 计算每个单元格的唯一路径数 - 3. 累加状态
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 返回右下角单元格的唯一路径数 - 4. 返回结果
    return dp[m - 1][n - 1]


def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        dp[0][i] = 1

    # 注意 从 1 开始, 因为第一行 第一列已经初始化了
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m-1][n-1]


"""
343 Integer Break
"""


def integerBreak(self, n: int) -> int:
    if n <= 3:
        return n - 1

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n+1):
        # j 是切下的第一块
        for j in range(1, i):
            # i-j 是剩下的部分, dp[i-j] 是剩下部分继续拆分能得到的最大乘积(前面我们已经求得, 可直接用)
            # 若此时 i = 12, j = 4, 不继续拆分：4 * 8 = 32, 若选择更多个小数乘(继续拆分8, 4*(3*3*2))：4 * dp[8],
            # dp[8]: 因为 8 可以拆成 3+3+2，乘积为 3×3×2=18, 4×18=72, 所以选择 4 * dp[8] = 72
            dp[i] = max(dp[i], j * max((i-j), dp[i-j]))
    return dp[n]


"""
96. Unique Binary Search Trees
"""


def numBST(n: int) -> int:
    # dp[i]表示i个节点能构成的不同BST的数量
    dp = [0] * (n + 1)
    dp[0] = 1  # 空树也是一种情况
    dp[1] = 1  # 只有一个节点的情况

    # 计算从2到n的每种情况
    for i in range(2, n + 1):
        # 选择不同的数字作为根节点
        for j in range(1, i + 1):
            # 左子树节点个数为j-1,右子树节点个数为i-j
            # 我们要的是多少个组合, 所以要左右想乘
            # 形成不同BST的数量只与节点个数有关,与具体的数字大小无关
            # 比如我们选择3作为根节点, 那左子树一定是用1和2这两个数,
            # 这两个数能形成的BST数量,和用4,5这两个数能形成的BST数量是完全一样的
            # 因为它们都是2个连续的数,只是大小不同而已
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]

















































