# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def rob(self, node):
        """
        :type node: TreeNode
        :rtype: int
        """
        if node is None:
            return 0

        val = 0

        if node.left is not None:
            val += self.rob(node.left.left) + self.rob(node.left.right)

        if node.right is not None:
            val += self.rob(node.right.left) + self.rob(node.left.right)

        return max(val + node.val, self.rob(node.left) + self.rob(node.right))


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, {})

    def traverse(self, node, map):
        if node is None:
            return 0
        if node in map:
            return map[node]

        val = 0

        if node.left is not None:
            val += self.traverse(node.left.left, map) + self.traverse(node.left.right, map)

        if node.right is not None:
            val += self.traverse(node.right.left, map) + self.traverse(node.right.right, map)

        val = max(val + node.val, self.traverse(node.left, map) + self.traverse(node.right, map))

        map[node] = val
        return val


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.right = TreeNode(1)
    print Solution().rob(tree)
