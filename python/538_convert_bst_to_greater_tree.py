# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.add = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.postoder(root)
        return root

    def postoder(self, node):
        if node is None:
            return
        self.postoder(node.right)
        node.val, self.add = node.val + self.add, self.add + node.val
        self.postoder(node.left)


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(13)
    print Solution().convertBST(tree)
