# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.view = []

    def rightSideView(self, root):

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rightSideViewTraverse(root, 1)
        return self.view

    def rightSideViewTraverse(self, node, height):
        if not node:
            return
        if height > len(self.view):
            self.view.append(node.val)
        self.rightSideViewTraverse(node.right, height + 1)
        self.rightSideViewTraverse(node.left, height + 1)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(5)
    tree.right.right = TreeNode(4)
    print Solution().rightSideView(tree)
