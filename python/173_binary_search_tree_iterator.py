# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.current = root
        """
        :type root: TreeNode
        """

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack or self.current

    def nextNode(self):
        """
        :rtype: int
        """
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        self.current = self.stack.pop()
        node = self.current
        self.current = self.current.right

        return node


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(4)
    right = tree.right
    right.left = TreeNode(3)
    right.right = TreeNode(5)

    i, v = BSTIterator(tree), []
    while i.hasNext():
        print i.nextNode().val
