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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode: 
        if inorder: 
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

  
if __name__ == "__main__": 
    res = Solution().buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
    print(res)
