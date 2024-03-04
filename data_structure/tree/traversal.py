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
    print(root.val, end=" ")


def pre_order_iter(root):
    if root is None:
        return []

    stack = []
    res = []
    stack.append(root)
    while stack:
        node_ = stack.pop()
        res.append(node_.val)
        if node_.right is not None:
            stack.append(node_.right)
        if node_.left is not None:
            stack.append(node_.left)

    return res


def in_order_iter(root):
    if not root:
        return []

    stack = []  # 不能提前将root结点加入stack中
    result = []
    cur = root
    while cur or stack:
        # 先迭代访问最底层的左子树结点
        if cur:
            stack.append(cur)
            cur = cur.left
        # 到达最左结点后处理栈顶结点
        else:
            cur = stack.pop()
            result.append(cur.val)
            # 取栈顶元素右结点
            cur = cur.right
    return result


def post_order_iter(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node_ = stack.pop()
        # 中结点先处理
        result.append(node_.val)
        # 左孩子先入栈
        if node_.left:
            stack.append(node_.left)
        # 右孩子后入栈
        if node_.right:
            stack.append(node_.right)
    # 将最终的数组翻转
    return result[::-1]


node = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(pre_order_iter(node))
pre_order(node)
