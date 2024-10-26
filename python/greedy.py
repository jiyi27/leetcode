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

# A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences. 
# 这句描述太有迷惑性了 
# 若数组含有一个数, 则返回1, 
# 这题的重要的点在于, [1, 1] 应该返回 1, 而不是0, 因为可以删除一个1,从而得到一个子序列 [1]
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        preDiff = 0
        curDiff = 0
        amount = 1
        for i in range(len(nums) - 1):
            curDiff = nums[i] - nums[i + 1]
            if (preDiff >= 0 and curDiff < 0) or (preDiff <= 0 and curDiff > 0):
                amount += 1
                preDiff = curDiff
        
        return amount


# test
print(Solution().wiggleMaxLength([1,1]))
