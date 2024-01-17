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
