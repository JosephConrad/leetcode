from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        largest = defaultdict(lambda: -1000000000000)
        self.largestHelper(root, 0, largest)
        return largest.values()

    def largestHelper(self, node, level, largest):
        if node is None:
            return
        largest[level] = max(node.val, largest[level])
        self.largestHelper(node.left, level + 1, largest)
        self.largestHelper(node.right, level + 1, largest)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(5)
    tree.right.left.left = TreeNode(7)
    tree.right.right = TreeNode(6)
    print Solution().largestValues(tree)
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print Solution().largestValues(tree)
    print Solution().largestValues(TreeNode(1))
    print Solution().largestValues(None)
    tree = TreeNode(1)
    tree.right = TreeNode(1)
    print Solution().largestValues(tree)
