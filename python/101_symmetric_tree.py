# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        return self.symmetric(root.left, root.right)

    def symmetric(self, l, r):
        if l is None and r is None:
            return True
        elif l is None or r is None:
            return False
        if l.val != r.val:
            return False
        return self.symmetric(l.left, r.right) and self.symmetric(r.left, l.right)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.right.right = TreeNode(1)
    print Solution().isSymmetric(tree)
