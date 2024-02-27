from collections import deque


def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def evalRPN(tokens):
    def resolves(a, b, Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return a - b
        elif Operator == '*':
            return a * b
        return int(a / b)

    stack = []
    for token in tokens:
        # 新知识, ord 用于返回指定字符的 Unicode 码点, 对于 ASCII 表中的字符, 其 Unicode 码点与 ASCII 码值是一样的
        # 在 Python 中，不能直接将字符串类型的字符与整数进行比较, 强类型, 与 C 不一样
        if len(token) == 1 and ord(token) < 48:
            integer2 = stack.pop()
            integer1 = stack.pop()
            operator = token
            resolved_ans = resolves(integer1, integer2, operator)
            stack.append(resolved_ans)
        else:
            stack.append(int(token))
    return stack.pop()


def removeDuplicatesTwoPointer(self, s):
    res = list(s)
    slow = fast = 0
    length = len(res)

    while fast < length:
        # 如果一样直接换，不一样会把后面的填在slow的位置
        res[slow] = res[fast]

        # 如果发现和前一个一样，就退一格指针
        if slow > 0 and res[slow] == res[slow - 1]:
            slow -= 1
        else:
            slow += 1
        fast += 1

    return ''.join(res[0: slow])


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
