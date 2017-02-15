# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findBottomHelper(root, 0)[0]

    def findBottomHelper(self, node, level):
        if node is None:
            return 0, -1
        if node.left is None and node.right is None:
            return node.val, level
        l = self.findBottomHelper(node.left, level + 1)
        r = self.findBottomHelper(node.right, level + 1)
        return l if l[1] >= r[1] else r


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(5)
    tree.right.left.left = TreeNode(7)
    tree.right.right = TreeNode(6)
    print Solution().findBottomLeftValue(tree)
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print Solution().findBottomLeftValue(tree)
    print Solution().findBottomLeftValue(TreeNode(1))
    print Solution().findBottomLeftValue(None)
    tree = TreeNode(1)
    tree.right = TreeNode(1)
    print Solution().findBottomLeftValue(tree)