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