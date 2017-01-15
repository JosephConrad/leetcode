import sys


#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.maks = -sys.maxint - 1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.calc(root)
        return self.maks

    def calc(self, node):
        if node is None:
            return 0
        v = node.val
        v_left = self.calc(node.left)
        v_right = self.calc(node.right)
        self.maks = max(self.maks, v_right + v_left + v, v_right + v, v_left + v, v)
        return max(max(v_left, v_right) + v, v)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().maxPathSum(tree)
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(6)
    print Solution().maxPathSum(tree)
    tree = TreeNode(2)
    tree.left = TreeNode(-1)
    print Solution().maxPathSum(tree)
    tree = TreeNode(1)
    tree.left = TreeNode(-2)
    tree.right = TreeNode(3)
    print Solution().maxPathSum(tree)
