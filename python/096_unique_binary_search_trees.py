import math


class Solution(object):
    def numTrees(self, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))


if __name__ == "__main__":
    print Solution().numTrees(0)
    print Solution().numTrees(1)
    print Solution().numTrees(2)
    print Solution().numTrees(3)
    print Solution().numTrees(5)
    print Solution().numTrees(15)
