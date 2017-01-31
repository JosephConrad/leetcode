class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.path(root, [], sum)

    def path(self, node, path, s):
        if node is None:
            return []

        path = path + [node.val]
        if node.left is None and node.right is None:
            return [path] if sum(path) == s else []

        return self.path(node.left, path, s) + self.path(node.right, path, s)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(1)
    tree.right.right = TreeNode(1)
    print Solution().pathSum(tree, 6)
