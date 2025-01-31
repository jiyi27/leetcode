def generateMatrix(self, n):
    """
    整体思路: 行负责每次都处理当前拐角, 列不负责
    假如4*4, layer = 0, 则此时列只负责 中间两个数据
    行处理完当前行所有数据 即四个
    """
    matrix = [[0] * n for _ in range(n)]  # syntax
    cur = 1
    layer = 0
    for round_ in range(0, n, 2):
        for i in range(layer, n - layer):
            matrix[layer][i], cur = cur, cur + 1

        if n - round_ <= 1:
            break

        # 只要第一次循环正确 之后也不会出错
        # 第一次 layer 为 0, n - layer - 1 = n -1 所以 matrix[i][n - layer - 1] 不会超出范围
        # 之后 layer = 2, 3 也不会超出范围 假如你前面的代码正确
        for i in range(layer + 1, n - layer - 1):
            matrix[i][n - layer - 1], cur = cur, cur + 1

        for i in range(n - layer - 1, layer - 1, -1):
            matrix[n - layer - 1][i], cur = cur, cur + 1

        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer], cur = cur, cur + 1

        layer += 1

    return matrix


def backspaceCompare(s, t):
    def processString(target):
        target_list = list(target)  # 将字符串转换为列表
        slow_index = 0
        for fast_index in range(len(target_list)):
            if target_list[fast_index] != '#':
                target_list[slow_index] = target_list[fast_index]
                slow_index += 1
            elif slow_index > 0:
                slow_index -= 1
        return ''.join(target_list[:slow_index])  # 将列表转换回字符串

    s = processString(s)
    t = processString(t)
    return s == t


def moveZeroes(nums):
    slow_index, fast_index = 0, 0
    for fast_index in range(len(nums)):
        if nums[fast_index] != 0:
            nums[slow_index] = nums[fast_index]
            slow_index += 1
    while slow_index < len(nums):
        nums[slow_index] = 0
        slow_index += 1


def removeElement(nums, val):
    slow_index = 0
    for fastIndex in range(len(nums)):
        if nums[fastIndex] != val:
            nums[slow_index] = nums[fastIndex]
            slow_index += 1
    return slow_index


def twoSum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [i, num_to_index[target - nums[i]]]
        num_to_index[nums[i]] = i
    return []


def longestCommonPrefix2(strs):
    res = strs[0]
    for i in range(1, len(strs)):
        while strs[i].startswith(res) is False:
            res = res[:-1]
    return res


def isValid(s):
    m1 = {')': '(', '}': '{', ']': '['}
    m2 = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in range(0, len(s)):
        if s[i] in m2:
            stack.append(s[i])
        elif len(stack) == 0 or m1[s[i]] != stack.pop():  # forget check if len(stack) == 0
            return False
    return len(stack) == 0


def mergeTwoLists(list1, list2):
    class ListNode:
        def __init__(self, val=0, next_=None):
            self.val = val
            self.next = next_

    cur = res = ListNode()
    while list1 and list2:
        if list1.val > list2.val:
            cur.next = list2
            list2, cur = list2.next, cur.next
        else:
            cur.next = list1
            list1, cur = list1.next, cur.next

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return res.next


def climbStairs(n):
    if n <= 2:
        return n

    prev1 = 1
    prev2 = 2
    for i in range(2, n):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2


def search(self, nums, target):
    left = 0
    right = len(nums) - 1  # 记得减1, 左闭右闭区间
    while left <= right:
        m = (left + right) // 2
        if target > nums[m]:
            left = m + 1
        elif target < nums[m]:
            right = m - 1
        else:
            return m
    return -1


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    # 最终跳出 while 循环时，一定有 left = right + 1
    # left 会指向 第一个大于等于 target 的位置，而 right 则会停在 比 target 小的最大值的位置
    # 所以我们应该把 target 放到 “比 target 小的最大值的位置” 前面, 也就是返回 left
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def mySqrt(target):
    """
    循环不变量: 若存在整数平方根, 则在 [lo, hi] 中
    循环结束, [hi, lo] 证明不存在整数平方根, 返回 hi
    """
    lo = 0
    hi = target
    while lo <= hi:
        m = (lo + hi) // 2
        if m * m < target:
            lo = m + 1
        elif m * m > target:
            hi = m - 1
        else:
            return m
    return hi


def searchRange(self, nums, target):
    def searchIndex(is_first=True):
        lo = 0
        hi = len(nums) - 1

        index = -1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] < target:
                lo = m + 1
            elif nums[m] > target:
                hi = m - 1
            else:
                index = m
                if is_first:
                    hi = m - 1
                else:
                    lo = m + 1
        return index

    first = searchIndex()
    last = searchIndex(False)

    return [first, last]
