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


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


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
    """
    在这个二分查找算法的实现中，最后返回 `hi + 1` 的逻辑是为了处理那些 `target` 不在数组 `nums` 中的情况。这个算法不仅用于查找元素，还用于确定如果要插入 `target` 到数组中，它应该插入的位置。这种情况可能发生在三种不同的场景：

    1. **`target` 小于数组中的任何一个数**：在这种情况下，循环结束时 `hi` 会变成 `-1`，因为 `lo` 会变成 `0` 并且 `hi` 会在下一次迭代中变成 `-1`。所以，`hi + 1` 会等于 `0`，这是 `target` 应该被插入的位置。

    2. **`target` 大于数组中的任何一个数**：在这种情况下，循环结束时 `lo` 会等于 `len(nums)`，因为 `target` 总是大于中间值，使得 `lo` 持续增加。由于循环条件是 `lo <= hi`，所以当 `lo` 变得比 `hi` 大时，循环结束。在这里，`hi + 1` 就等于 `lo`，即数组的长度，这是 `target` 应该被插入的位置。

    3. **`target` 应该被插入数组中间的某个位置**：在这种情况下，`target` 介于两个数组元素之间。循环结束时，`lo` 将指向较大的那个元素，而 `hi` 将指向较小的那个元素。因此，`hi + 1` 将是 `target` 应该插入的正确位置。

    总之，`return hi + 1` 确保了无论 `target` 的值是什么，算法都能返回正确的插入位置，无论它是否存在于数组中。这使得这个函数非常适合用于实现如排序数组的插入操作等场景。
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if target > nums[m]:
            lo = m + 1
        elif target < nums[m]:
            hi = m - 1
        else:
            return m  # target 等于数组中的某个数
    return hi + 1


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