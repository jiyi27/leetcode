def twoSum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [i, num_to_index[target-nums[i]]]
        num_to_index[nums[i]] = i
    return []

