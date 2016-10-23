# 129. Sum Root to Leaf Numbers   QuestionEditorial Solution  My Submissions

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
#   could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        return self.traverse(root, [])

    def traverse(self, node, path):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return int(''.join(map(str, path + [node.val])))

        return self.solve(node.left, path + [node.val]) + self.solve(node.right, path + [node.val])


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    print Solution().sumNumbers(tree)
