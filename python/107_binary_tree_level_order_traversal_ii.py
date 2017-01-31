import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = Queue.Queue()
        queue.put(root)
        queue.put('#')
        result = []
        current = []
        while not queue.empty():
            node = queue.get()
            if node is '#':
                result.append(current)
                current = []
                if not queue.empty():
                    queue.put('#')
                continue

            current.append(node.val)
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        return result[::-1]


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    tree.left.right.left = TreeNode(1)
    print Solution().levelOrder(tree)
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    print Solution().levelOrder(tree)
    print Solution().levelOrder(None)
