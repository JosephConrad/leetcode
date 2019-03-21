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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode: 
        if inorder: 
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root

  
if __name__ == "__main__": 
    res = Solution().buildTree(inorder=[9,3,15,20,7], postorder=[9,15,7,20,3])
    print(res)
