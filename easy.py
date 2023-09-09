def twoSum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [i, num_to_index[target-nums[i]]]
        num_to_index[nums[i]] = i
    return []


def romanToInt(s):
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = m[s[len(s) - 1]]
    for i in reversed(range(len(s) - 1)):
        if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
            res -= 1
        elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
            res -= 10
        elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
            res -= 100
        else:
            res += m[s[i]]
    return res
