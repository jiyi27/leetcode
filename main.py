class Solution:
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
