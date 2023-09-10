def twoSum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [i, num_to_index[target - nums[i]]]
        num_to_index[nums[i]] = i
    return []


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    ans = strs[0]
    for i in range(1, len(strs)):
        while ans != strs[i][:len(ans)]:
            ans = ans[:-1]
            if ans == '':
                return ''
    return ans
