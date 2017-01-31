class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.balanced(root) > -1

    def balanced(self, node):
        if node is None:
            return 0
        h1 = self.balanced(node.left)
        h2 = self.balanced(node.right)
        if abs(h1 - h2) <= 1 and h1 >= 0 and h2 >= 0:
            return max(h1, h2) + 1
        return -1


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().isBalanced(tree)
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().isBalanced(tree)
