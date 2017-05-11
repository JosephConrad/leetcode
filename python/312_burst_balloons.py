class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + filter(lambda x: x != 0, nums) + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]


if __name__ == "__main__":
    print Solution().maxCoins(nums=[3, 1, 5, 8])
