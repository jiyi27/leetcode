from collections import deque


def maxDepth(root):
    if not root:
        return 0

    q = deque()
    d = 0
    q.append(root)
    while q:
        for i in range(len(q)):
            node_ = q.popleft()
            if node_.left:
                q.append(node_.left)
            if node_.right:
                q.append(node_.right)
        d += 1
    return d


class Solution104:
    def getDepth(self, node_):
        if not node_:
            return 0
        left_height = self.getDepth(node_.left)
        right_height = self.getDepth(node_.right)
        return 1 + max(left_height, right_height)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)


class Solution1:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val
                and self.isMirror(left.right, right.left)
                and self.isMirror(left.left, right.right))

    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)


def invertTree(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        # invert
        node_ = queue.popleft()
        temp_node = node_.left
        node_.left = node_.right
        node_.right = temp_node

        if node_.left:
            queue.append(node_.left)
        if node_.right:
            queue.append(node_.right)
    return root


def postorderTraversal(root):
    def traverse(res_, node):
        if node is None:
            return
        traverse(res_, node.left)
        traverse(res_, node.right)
        res_.append(node.val)

    res = []
    traverse(res, root)
    return res


def preorderTraversal(root):
    def traverse(res_, node):
        if node is None:
            return
        res_.append(node.val)
        traverse(res_, node.left)
        traverse(res_, node.right)

    res = []
    traverse(res, root)
    return res


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right