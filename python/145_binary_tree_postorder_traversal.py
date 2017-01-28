# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder = []
        self.postorder(postorder, root)
        return postorder

    def postorder(self, acc, node):
        if node is None:
            return
        self.postorder(acc, node.left)
        self.postorder(acc, node.right)
        acc.append(node.val)


if __name__ == "__main__":
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print Solution().postorderTraversal(tree)
