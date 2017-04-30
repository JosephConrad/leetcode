# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 1
        self.traverse(root)
        return self.result - 1

    def traverse(self, node):
        if not node:
            return 0
        length_left = self.traverse(node.left)
        length_right = self.traverse(node.right)
        self.result = max(self.result, length_left + length_right + 1)
        return max(length_left, length_right) + 1


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    tree.left.right.left = TreeNode(1)
    print Solution().diameterOfBinaryTree(tree)
