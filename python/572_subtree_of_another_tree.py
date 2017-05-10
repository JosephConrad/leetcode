# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s1 = ''.join(self.preorder(s))
        s2 = ''.join(self.preorder(t))
        return s2 in s1

    def preorder(self, node):
        return ["^"] + [str(node.val)] + ["#"] + self.preorder(node.left) + self.preorder(node.right) if node else ['$']


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    tree.left.right.left = TreeNode(1)
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(5)
    print Solution().isSubtree(tree, tree1)
