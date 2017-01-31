class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, node, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True if sum - node.val == 0 else False
        return self.hasPathSum(node.left, sum - node.val) or self.hasPathSum(node.right, sum - node.val)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    print Solution().hasPathSum(tree, 12)
    print Solution().hasPathSum(tree, 9)
    print Solution().hasPathSum(tree, 6)
    print Solution().hasPathSum(tree, 0)
    print Solution().hasPathSum(None, 0)
