#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    lexMin = None

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallestFromLeafHelper(root, '')
        return self.lexMin

    def smallestFromLeafHelper(self, node: TreeNode, stack: str) -> str:
        if not node:
            return
        newStack = chr(node.val + ord('a')) + stack 
        if node.left is None and node.right is None: 
            if not self.lexMin or newStack < self.lexMin: 
                self.lexMin = newStack 
        self.smallestFromLeafHelper(node.left, newStack)
        self.smallestFromLeafHelper(node.right, newStack)





if __name__ == "__main__":
    #[25,1,3,1,3,0,2]
    tree = TreeNode(25)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(2)
    print(Solution().smallestFromLeaf(tree))

    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)
    print(Solution().smallestFromLeaf(tree))
