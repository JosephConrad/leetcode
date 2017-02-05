# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.genTrees(1, n)

    def genTrees(self, left, right):
        trees = []
        if left > right:
            trees.append(None)

        for i in range(left, right + 1):
            left_list = self.genTrees(left, i - 1)
            right_list = self.genTrees(i + 1, right)
            for l in left_list:
                for r in right_list:
                    t = TreeNode(i)
                    t.left = l
                    t.right = r
                    trees.append(t)
        return trees


if __name__ == "__main__":
    print Solution().generateTrees(3)