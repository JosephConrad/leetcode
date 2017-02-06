# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, sum, 0)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.result

    def dfs(self, node, target, path):
        if not node:
            return

        new_path = path + node.val
        if new_path == target:
            self.result += 1
        self.dfs(node.left, target, new_path)
        self.dfs(node.right, target, new_path)


if __name__ == "__main__":
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(2)
    tree.left.right.right = TreeNode(1)
    tree.left.left.left = TreeNode(3)
    tree.left.left.right = TreeNode(-2)
    tree.right = TreeNode(-3)
    tree.right.right = TreeNode(11)
    print Solution().pathSum(tree, 8)

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(3)
    print Solution().pathSum(tree, 3)
