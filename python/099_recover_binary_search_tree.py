# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.val) + "\n"
        for child in [self.left, self.right]:
            if child:
                ret += child.__str__(level + 1)
        return ret


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodes = self.inorder(root)
        for i, node in zip(sorted(map(lambda x: x.val, nodes)), nodes):
            node.val = i

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node] + self.inorder(node.right)


if __name__ == "__main__":
    if __name__ == "__main__":
        tree = TreeNode(3)
        tree.left = TreeNode(2)
        tree.right = TreeNode(1)
        tree.left.left = TreeNode(4)
        tree.left.left.left = TreeNode(0)
        tree.right.right = TreeNode(5)
        Solution().recoverTree(tree)
        tree = TreeNode(3)
        tree.left = TreeNode(2)
        tree.right = TreeNode(1)
        Solution().recoverTree(tree)
        Solution().recoverTree([])
