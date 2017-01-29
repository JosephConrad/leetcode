# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.stack = [root] if root is not None else []
        self.visited = set()
        """
        :type root: TreeNode
        """

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) is not 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack[-1]
        while node.left and node.left not in self.visited:
            l = node.left
            self.stack.append(l)
            self.visited.add(l)
            node = l
        result = node.val
        self.stack.pop()
        if node.right:
            self.stack.append(node.right)
        return result


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    i, v = BSTIterator(tree), []
    while i.hasNext():
        v.append(i.next())
    print v

    i, v = BSTIterator(None), []
    while i.hasNext():
        v.append(i.next())
    print v
