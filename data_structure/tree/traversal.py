from collections import deque


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        cur_node = queue.popleft()
        res.append(cur_node.val)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return res


def pre_order(root):
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


node = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
in_order(node)
