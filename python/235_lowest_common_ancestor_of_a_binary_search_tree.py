# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lowestCommon(root, p, q)
        return self.result

    def lowestCommon(self, node, p, q):
        if node is None:
            return False, False
        l1, r1 = self.lowestCommon(node.left, p, q)
        l2, r2 = self.lowestCommon(node.right, p, q)
        l3, r3 = False, False
        if p is node:
            l3 = True
        if q is node:
            r3 = True
        if (l1 or l2 or l3) and (r1 or r2 or r3) and self.result is None:
            self.result = node
        return (l1 or l2 or l3), (r1 or r2 or r3)


if __name__ == "__main__":
    tree = TreeNode(6)
    x = p = tree.left = TreeNode(2)
    q = tree.right = TreeNode(8)
    tree.left.left = TreeNode(0)
    y = tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)
    print Solution().lowestCommonAncestor(tree, p, q)
    print Solution().lowestCommonAncestor(tree, x, y)
