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
