from collections import Counter


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        freq = dict()
        self.findFrequency(root, freq)
        maks = max(freq.values())
        return [k for k, v in freq.items() if v == maks]

    def findFrequency(self, node, freq):
        if not node:
            return 0

        sum_left = self.findFrequency(node.left, freq)
        sum_right = self.findFrequency(node.right, freq)
        my_sum = sum_left + node.val + sum_right
        freq[my_sum] = freq.get(my_sum, 0) + 1
        return my_sum


class Solution2(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        subsums = []
        self.findSubsums(root, subsums)
        data = Counter(subsums)
        maks = 0
        result = []
        for elt in data.most_common():
            maks = max(maks, elt[1])
            if elt[1] == maks:
                result.append(elt[0])
        return result

    def findSubsums(self, node, subsums):
        if not node:
            return 0

        sum_left = self.findSubsums(node.left, subsums)
        sum_right = self.findSubsums(node.right, subsums)
        my_sum = sum_left + node.val + sum_right
        subsums.append(my_sum)
        return my_sum


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(-5)
    print Solution().findFrequentTreeSum(tree)
    print Solution().findFrequentTreeSum(None)
