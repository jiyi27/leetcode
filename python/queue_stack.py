from collections import deque


def removeDuplicates(s):
    res = list()
    for item in s:
        if res and res[-1] == item:
            res.pop()
        else:
            res.append(item)
    return "".join(res)  # 字符串拼接


class MyStack(object):

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in  # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()

    def top(self):
        """
        :rtype: int
        """
        # 写法一：
        if self.empty():
            return None

        return self.queue_in[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue_in) == 0


class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        if not self.stack_out:
            # Transfer from enqueue stack to dequeue stack
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # Dequeue operation
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        val = self.pop()
        self.stack_out.append(val)
        return val

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stack_in or self.stack_out)
