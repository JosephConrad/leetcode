# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    list_head = None

    def flatten(self, node):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if node is None:
            return
        self.flatten(node.right)
        self.flatten(node.left)
        node.right = self.list_head
        node.left = None
        self.list_head = node
        return


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(6)
    Solution().flatten(tree)