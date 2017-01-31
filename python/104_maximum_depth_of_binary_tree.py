class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        if node is None:
            return 0
        h1 = self.maxDepth(node.left)
        h2 = self.maxDepth(node.right)
        return max(h1, h2) + 1


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    tree.left.right.left = TreeNode(1)
    print Solution().maxDepth(tree)
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().maxDepth(tree)
    print Solution().maxDepth(None)
