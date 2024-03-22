from collections import deque


class Solution98:
    def isValidBST(self, root):
        if not root:
            return True

        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)
        return left and right


class Solution700:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)


class Solution617:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


def constructMaximumBinaryTree654(nums):
    def buildTree(arr):
        if not arr:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        max_num = arr[0]
        max_index = 0
        for i in range(1, len(arr)):
            if max_num < arr[i]:
                max_num = arr[i]
                max_index = i

        node = TreeNode(arr[max_index])
        node.left = buildTree(arr[:max_index])
        node.right = buildTree(arr[max_index + 1:])
        return node

    return buildTree(nums)


class Solution106:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid+1:len(postorder) - 1])
        return root


class Solution105:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


def hasPathSum112(root, targetSum):
    def travel(node, sum_):
        sum_ += node.val

        if not node.left and not node.right:
            if sum_ == targetSum:
                return True
            return False

        if node.left:
            if travel(node.left, sum_):
                return True
        if node.right:
            if travel(node.right, sum_):
                return True
        return False

    if not root:
        return False
    return travel(root, 0)


class Solution513:
    def __init__(self):
        self.max_depth = -1
        self.res = None

    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = node.val
            return
        if node.left:
            # you can simply replace with: self.traversal(node.right, depth + 1)
            # 这里只是为了表示回溯
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1

    def findBottomLeftValue(self, root):
        self.traversal(root, 0)
        return self.res


def sumOfLeftLeaves(root):
    if not root:
        return 0

    def dfs(node, sum__):
        if node.left and not node.left.left and not node.left.right:
            sum__[0] += node.left.val
        if node.left:
            dfs(node.left, sum__)
        if node.right:
            dfs(node.right, sum__)

    sum_ = [0]
    dfs(root, sum_)
    return sum_[0]


class Solution257:
    def travel_node(self, node, path, res):
        path.append(node.val)
        if not node.left and not node.right:
            res.append('->'.join([str(val) for val in path]))
            return

        if node.left:
            self.travel_node(node.left, path, res)
            path.pop()
        if node.right:
            self.travel_node(node.right, path, res)
            path.pop()

    def binaryTreePaths(self, root):
        res = []
        path = []
        if not root:
            return res

        self.travel_node(root, path, res)
        return res


class Solution110(object):
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    def isBalanced(self, root):
        return self.getHeight(root) != -1


class Solution222(object):
    def count(self, node):
        if not node:
            return 0
        left = self.count(node.left)
        right = self.count(node.right)
        return left + right + 1

    def countNodes(self, root):
        return self.count(root)


def countNodes222(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    num_nodes = 0
    while queue:
        num_nodes += 1
        node_ = queue.popleft()
        if node_.left:
            queue.append(node_.left)
        if node_.right:
            queue.append(node_.right)
    return num_nodes


class Solution111:
    def __init__(self):
        self.result = float('inf')
        self.depth = 0.0

    def minDepth(self, root):
        def getDepth(node):
            self.depth += 1
            if not node.left and not node.right:
                self.result = min(self.depth, self.result)
                return

            if node.left:
                getDepth(node.left)
                self.depth -= 1
            if node.right:
                getDepth(node.right)
                self.depth -= 1

        if not root:
            return 0
        getDepth(root)
        return int(self.result)


def minDepth111(root):
    if not root:
        return 0
    queue = deque()
    min_d = 0
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            node_ = queue.popleft()
            if not node_.left and not node_.right:
                return min_d + 1
            if node_.left:
                queue.append(node_.left)
            if node_.right:
                queue.append(node_.right)
        min_d += 1
    return min_d


class Solution104:
    def __init__(self):
        self.depth = 0
        self.result = -1

    def maxDepth(self, root):
        def getDepth(node):
            if not node:
                return

            self.depth += 1
            if self.result < self.depth:
                self.result = self.depth

            if node.left:
                getDepth(node.left)
                self.depth -= 1
            if node.right:
                getDepth(node.right)
                self.depth -= 1

        getDepth(root)
        return self.depth


class SmpleSolution104:
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


def maxDepth104(root):
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
