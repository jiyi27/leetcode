def getIntersectionNode(headA, headB):
    len_a = len_b = 0
    cur = headA
    while cur:
        len_a, cur = len_a + 1, cur.next
    cur = headB
    while cur:
        len_b, cur = len_b + 1, cur.next

    cur_a, cur_b = headA, headB
    if len_b > len_a:
        len_a, len_b = len_b, len_a
        cur_a, cur_b = headB, headA

    for _ in range(len_a - len_b):
        cur_a = cur_a.next

    while cur_a:
        if cur_a == cur_b:
            return cur_a
        cur_a, cur_b = cur_a.next, cur_b.next
    return None


def removeNthFromEnd(head, n):
    pre = dummy_head = ListNode(next=head)
    slow_pointer = fast_pointer = head
    distance = 0
    while fast_pointer:
        fast_pointer = fast_pointer.next
        distance += 1
        if distance > n:
            pre = slow_pointer
            slow_pointer = slow_pointer.next
            distance -= 1
    pre.next = slow_pointer.next
    return dummy_head.next


def swapPairs(head):
    dummy_head = ListNode(next=head)
    pre, cur = dummy_head, head
    while cur and cur.next:
        # save
        temp1 = cur.next
        temp2 = cur.next.next
        # swap
        cur.next = temp2
        temp1.next = cur
        pre.next = temp1
        # move
        pre = cur
        cur = temp2

    return dummy_head.next


def reverseList(head):
    pre = None
    cur = head
    # 思路: 仅仅改变指针方向便可以
    while cur:
        temp = cur.next
        cur.next = pre
        pre, cur = cur, temp
    return pre


class MyLinkedList(object):
    class ListNode:
        def __init__(self, val, next_=None):
            self.val = val
            self.next = next_

    def __init__(self):
        self.size = 0
        self.dummy_head = self.ListNode(None)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        temp = self.dummy_head.next
        val = temp.val
        while index > 0:
            temp, index = temp.next, index - 1
            val = temp.val
        return val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = self.ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        temp = self.dummy_head
        for _ in range(self.size):
            temp = temp.next
        temp.next = self.ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0:
            return
        if index == self.size:
            self.addAtTail(val)
            return

        temp = self.dummy_head
        while index > 0:
            temp, index = temp.next, index - 1
        temp.next = self.ListNode(val, temp.next)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return

        temp = self.dummy_head
        while index > 0:
            temp, index = temp.next, index - 1
        temp.next = temp.next.next
        self.size -= 1


def removeElements(self, head, val):
    class ListNode(object):
        def __init__(self, val_=0, next_=None):
            self.val = val_
            self.next = next_

    cur = dummy_head = ListNode(next_=head)
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
