def fourSumCount(nums1, nums2, nums3, nums4):
    record = {}
    for i in nums1:
        for j in nums2:
            if i + j in record:
                record[i + j] += 1
            else:
                record[i + j] = 1
    count = 0
    for i in nums3:
        for j in nums4:
            if -(i + j) in record:
                count += record[-(i + j)]
    return count


def twoSum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return []


def isHappy(n):
    record = {n}
    while True:
        sum_square = 0
        while n:
            remainder = n % 10
            n = n // 10
            sum_square += remainder * remainder

        if sum_square == 1:
            return True
        if sum_square in record:
            return False
        record.add(sum_square)
        n = sum_square


def intersection(nums1, nums2):
    res = set()
    record = {}
    for num in nums1:
        record[num] = 1
    for num in nums2:
        if num in record and record[num] == 1:
            res.add(num)
    return list(res)


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    record = [0] * 26
    for c in s:
        record[ord(c) - ord('a')] += 1
    for c in t:
        record[ord(c) - ord('a')] -= 1
    for i in range(26):
        if record[i] != 0:
            return False
    return True
