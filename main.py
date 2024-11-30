def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        else:
            dp[i][0] = 1
    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        else:
            dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m-1][n-1]
