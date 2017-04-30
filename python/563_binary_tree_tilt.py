# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        self.tilt(root, result)
        return result[0]

    def tilt(self, node, result):
        if not node:
            return 0
        l = self.tilt(node.left, result)
        r = self.tilt(node.right, result)
        result[0] += abs(l - r)
        return l + r + node.val


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    print Solution().findTilt(tree)
