from typing import List


def GiveCandy(g: [int], s: [int]) -> int:
    g.sort()
    s.sort()

    index = 0
    for i in range(len(s)):
        if index < len(g) and g[index] <= s[i]:
            index += 1
    return index

    return 0


# A sequence with one element and a sequence with
# two non-equal elements are trivially wiggle sequences.
# 这句描述太有迷惑性了
# 若数组含有一个数, 则返回1
# 这题的重要的点在于, [1, 1] 应该返回 1, 而不是0, 因为可以删除一个1,从而得到一个子序列 [1]
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        preDiff = 0  # 技巧1, 使用 preDiff 记录前一个差值, 避免重复计算
        curDiff = 0
        amount = 1  # 核心在于此, 即只要数组有值, 则至少有一个子序列
        for i in range(len(nums) - 1):
            curDiff = nums[i] - nums[i + 1]
            if (preDiff >= 0 and curDiff < 0) or (preDiff <= 0 and curDiff > 0):
                amount += 1
                preDiff = curDiff

        return amount


def maxSubArrayBruteForce(nums: List[int]) -> int:
    max = float('-inf')
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            if cur_sum > max:
                max = cur_sum
    return max


# 核心在于 两个若此刻总和小于0, 则往后加 肯定让总和更小, 因此应果断舍弃
# 前面已经保存了最大结果, 所以不用担心漏掉数据
def maxSubArray(nums: List[int]) -> int:
    # float('-inf') 常用到, 应该记住
    max_sum = float('-inf')
    cur_sum = 0
    for num in nums:
        # 注意这俩语句的顺序, 很重要, 反过来, 则最后一次遍历不会运行 max_sum = cur_sum
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum


# 可以延伸出另一个写法
def maxSubArray2(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    cur_sum = max_sum = nums[0]
    for num in nums:
        # cur_sum = num 只有一种情况, 即 cur_sum 为负数, 因此需要舍弃
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


# 假如数组为 [1, 2, 7, 9], 第一天买到最后一天卖
# 或 第一天买, 第二天卖, 依次类推. 为什么赚的和第次策略一样多?
# 想像成一个直方图 📊, 累计增高和一次增高 其实 差距是一样的
def maxProfit(self, prices: List[int]) -> int:
    sum = 0
    for i in range(1, len(prices)):
        sum = max(sum + prices[i] - prices[i-1], sum)
    return sum

    