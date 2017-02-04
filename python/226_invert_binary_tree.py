# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(7)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(9)
    tree.left.right = TreeNode(6)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(1)
    inverted = Solution().invertTree(tree)
