import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(n + m - 2) / (math.factorial(n - 1) * math.factorial(m - 1))


if __name__ == "__main__":
    print Solution().uniquePaths(3, 7)
    print Solution().uniquePaths(1, 1)
    print Solution().uniquePaths(2, 2)
