# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = self.inorder(root)
        return min([abs(nodes[i] - nodes[i-1]) for i in range(1, len(nodes))])

    def inorder(self, root):
        return [] if root is None else self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.right.right = TreeNode(1)
    print Solution().getMinimumDifference(tree)
