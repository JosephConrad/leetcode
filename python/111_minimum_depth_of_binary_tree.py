class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.minDepthNode(root, 1)

    def minDepthNode(self, node, height):
        if node.left is None and node.right is None:
            return height
        if node.right is None:
            return self.minDepthNode(node.left, height + 1)
        if node.left is None:
            return self.minDepthNode(node.right, height + 1)
        return min(self.minDepthNode(node.left, height + 1), self.minDepthNode(node.right, height + 1))


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().minDepth(tree)
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().minDepth(tree)
