class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        acc = []
        self.inorder(root, acc)
        mode, global_max, local_max = [acc[0]], 1, 1
        for i in range(1, len(acc)):
            local_max = local_max + 1 if acc[i] == acc[i - 1] else 1
            if local_max > global_max:
                mode = [acc[i]]
            if global_max == local_max:
                mode.append(acc[i])
            global_max = max(global_max, local_max)

        return mode

    def inorder(self, node, acc):
        if node is None:
            return
        self.inorder(node.left, acc)
        acc.append(node.val)
        self.inorder(node.right, acc)


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(3)
    print Solution().findMode(tree)
