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