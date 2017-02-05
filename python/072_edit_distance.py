class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        k, l = len(word1), len(word2)
        dp = [[0] * (l + 1) for _ in range(k + 1)]

        for i in range(k + 1):
            dp[i][0] = i
        for i in range(l + 1):
            dp[0][i] = i

        for i in range(1, k + 1):
            for j in range(1, l + 1):
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1,
                               dp[i - 1][j - 1] + int(not word1[i - 1] == word2[j - 1]))

        return dp[-1][-1]


if __name__ == "__main__":
    print Solution().minDistance("ala", "aram")
    print Solution().minDistance("horse", "ros")
    print Solution().minDistance("", "a")
