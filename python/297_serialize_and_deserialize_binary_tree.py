# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ' '.join(self.inorder(root))

    def inorder(self, node):
        return [str(node.val)] + self.inorder(node.left) + self.inorder(node.right) if node else ['#']

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.traverse(iter(data.split()))

    def traverse(self, values):
        if values:
            elt = next(values)
            if elt == '#':
                return None
            node = TreeNode(int(elt))
            node.left = self.traverse(values)
            node.right = self.traverse(values)
            return node


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.right.right = TreeNode(1)

    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    codec.deserialize(codec.serialize(tree))

    print codec.serialize(tree)
    print codec.deserialize(codec.serialize(tree))
    print codec.serialize(codec.deserialize(codec.serialize(tree)))
