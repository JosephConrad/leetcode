# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, node, isLeft=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val if isLeft else 0
        return self.sumOfLeftLeaves(node.left, True) + self.sumOfLeftLeaves(node.right, False)


class Solution2(object):
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root, False)
        return self.total

    def traverse(self, node, isLeft):
        if not node:
            return
        if not node.left and not node.right:
            self.total += node.val if isLeft else 0
            return
        self.traverse(node.left, True)
        self.traverse(node.right, False)


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print Solution().sumOfLeftLeaves(tree)
    print Solution().sumOfLeftLeaves(None)
