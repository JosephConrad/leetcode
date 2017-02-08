# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, acc, result):
        if node is None:
            return
        if not node.left and not node.right:
            result.append('->'.join(acc + [str(node.val)]))
            return
        self.dfs(node.left, acc + [str(node.val)], result)
        self.dfs(node.right, acc + [str(node.val)], result)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().binaryTreePaths(tree)
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(5)
    print Solution().binaryTreePaths(tree)
