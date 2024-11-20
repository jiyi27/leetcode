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
def wiggleMaxLength(nums: List[int]) -> int:
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


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    cover = 0

    for i in range(len(nums)):
        if i > cover:
            break
        cover = max(nums[i] + i, cover)
        if cover >= len(nums) - 1:
            return True
    return False


def canJumpSolution2(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    cover = 0
    i = 0

    while i <= cover:
        cover = max(cover, nums[i] + i)
        if cover >= len(nums):
            return True
        i += 1
    return False


def jump2(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    cur_distance = 0
    next_distance = 0
    ans = 0
    for i in range(len(nums)):
        next_distance = max(nums[i] + i, next_distance)
        if i == cur_distance:
            cur_distance = next_distance
            ans += 1
            if next_distance >= len(nums - 1):
                break
    return ans


def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort(key=lambda x: abs(x), reverse=True)
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = nums[i] * -1
            k -= 1
    if k % 2 == 1:
        nums[-1] = nums[-1] * -1
    return sum(nums)


# ----------------------- canCompleteCircuitBruteForce -----------------------
# 找出逻辑错误,
# 看着像遍历了一圈, 其实但实际上它并没有完整地走完一圈，
# j 每次改变后 j = j % len(gas), 重新进入 for 循环, j 的值已经改变了, 比如原来是len(gas),
# 求余后=0, 则进入循环又从1开始而不是 len(gas) + 1, 这样循环就没办法结束
def canCompleteCircuitWithError(gas: List[int], cost: List[int]) -> int:
    for i in range(len(gas)):
        total_gas = 0
        for j in range(i, i + len(gas)):
            j = j % len(gas)
            total_gas += gas[j] - cost[j]
            if total_gas < 0:
                break
        if total_gas >= 0:
            return i
    return -1


# 正确做法, 使用新的变量 idx 来作为索引, 不改变 j
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    for i in range(len(gas)):
        total_gas = 0
        for j in range(i, i + len(gas)):
            idx = j % len(gas)
            total_gas += gas[idx] - cost[idx]
            if total_gas < 0:
                break
        if total_gas >= 0:
            return i
    return -1


# 为什么不重置 total_gas
# total_gas 累加每一站的净油量（gas[i] - cost[i]），并且在整个行程中不重置。
# 这是因为它用于全局判断：如果总油量 total_gas 小于 0，说明油量不足，无法完成一圈，直接返回 -1。
# 而如果 total_gas 大于等于 0，则说明总油量足够，那么一定存在一个有效的起点，使得从该起点可以完成一圈。
def canCompleteCircuitSolution2(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start = 0
    total_gas = 0
    current_gas = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        # 当前累加current_gas一旦小于0，起始位置变为i+1，因为从 [start, i] 之间开始一定不行
        if current_gas < 0:
            start = i + 1
            current_gas = 0
    return start if total_gas >= 0 else -1

# ----------------------------------- END -----------------------------------


# 刚开始的思路是 在一次遍历中 怎么根据两侧的大小给它值
# 其实 分开遍历 左右一遍一次才是正解
def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    candy_array = [1] * n

    # 从左往右遍历, 比较右侧是否大于左侧
    for i in range(n - 1):
        if ratings[i + 1] > ratings[i]:
            candy_array[i+1] = candy_array[i] + 1

    # 从右往左遍历, 比较左侧是否大于右侧, 错误方法(思考为什么这样是错误的):
    # for i in range(n - 1, -1, -1):
    #    if ratings[i] > ratings[i - 1]:
    for i in range(n - 2, -1, -1):  # 修改遍历范围
        if ratings[i] > ratings[i + 1]:  # 修改比较方向
            candy_array[i] = max(candy_array[i], candy_array[i + 1] + 1)
    return sum(candy_array)


def lemonadeChange(bills: List[int]) -> bool:
    if not bills:
        return True
    if bills[0] > 5:
        return False

    balance = [0] * 21

    for bill in bills:
        balance[bill] += 1
        if bill == 10:
            if balance[5] > 0:
                balance[5] -= 1
            else:
                return False
        elif bill == 20:
            if balance[10] > 0 and balance[5] > 0:
                balance[10] -= 1
                balance[5] -= 1
            elif balance[5] >= 3:
                balance[5] -= 3
            else:
                return False
    return True
