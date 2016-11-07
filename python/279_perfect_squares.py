# 279. Perfect Squares
#
# Given a positive integer n, find the least number of perfect square numbers
#     (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
#     return 2 because 13 = 4 + 9.


class Solution(object):
    dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(len(Solution.dp), n + 1):
            minimum = 100000
            j = 1
            while j * j <= i:
                minimum = min(minimum, Solution.dp[i - j * j] + 1)
                j += 1
            Solution.dp.append(minimum)
        return Solution.dp[n]


if __name__ == "__main__":
    print Solution().numSquares(12)
    print Solution().numSquares(13)
    print Solution().numSquares(0)
