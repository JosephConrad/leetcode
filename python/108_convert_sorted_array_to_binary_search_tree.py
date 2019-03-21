# Definition for a binary tree node. 

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self): 
        if self is None:
            return 'None'
        else:
            return self.printTree(self, 0)

    def printTree(self, node, depth):
        if node is None:
            return ''
        strNode = '{} -> {}\n'.format('    '*depth, node.val)
        strLeft = self.printTree(node.left, depth + 1)
        strRight = self.printTree(node.right, depth + 1)
        return strNode + strLeft + strRight

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        


if __name__ == "__main__":
    print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
        