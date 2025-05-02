def fourSum(nums, target):
    nums.sort()
    output = []
    for i in range(len(nums)):
        if nums[i] > target > 0 and nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] > target >= 0:
                break
            # i 是外层循环的索引，代表四元组中的第一个数字的位置。j 作为第二个数字的索引，至少需要是 i + 1（即第一个数字之后的位置）
            if j > i + 1 and nums[j] == nums[j - 1]:  # 注意这里不是 j > 0
                continue

            left = j + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    output.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return output


# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         record = {}
#         res = set()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 v = nums[i] + nums[j]
#                 if v in record:
#                     record[v].append({i, j})
#                 else:
#                     record[v] = [{i, j}]
#         for i in range(len(nums)):
#             if -nums[i] in record:
#                 for index_set in record[-nums[i]]:
#                     if i in index_set:
#                         continue
#                     else:
#                         index_list = list(index_set)
#                         res.add((nums[index_list[0]], nums[index_list[1]], nums[i]))
#         res = list(res)
#         return res
def threeSum(nums):
    target = 0
    nums.sort()
    result = []
    for i in range(len(nums)):
        # 如果第一个元素已经大于0，不需要进一步检查
        if nums[i] > 0:
            return result

        # 跳过相同的元素以避免重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum_ = nums[i] + nums[j] + nums[k]
            if sum_ == target:
                result.append((nums[i], nums[j], nums[k]))
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif sum_ < target:
                j += 1
            else:
                k -= 1
    return result


def canConstruct(ransomNote, magazine):
    record = {}
    for c in magazine:
        if c in record:
            record[c] += 1
        else:
            record[c] = 1
    for c in ransomNote:
        if c in record and record[c] > 0:
            record[c] -= 1
        else:
            return False
    return True


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
