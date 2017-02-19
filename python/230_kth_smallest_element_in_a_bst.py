# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder = self.inOrder(root)
        return inorder[k-1] if k <= len(inorder) else 0

    def inOrder(self, node):
        if not node:
            return []
        return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().kthSmallest(tree, 4)
    print Solution().kthSmallest(None, 4)
