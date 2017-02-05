class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        k = len(s1) + 1
        l = len(s2) + 1
        dp = [[False for _ in range(l)] for _ in range(k)]

        dp[0][0] = True

        for i in range(1, k):
            if dp[i-1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for i in range(1, l):
            if dp[0][i-1] and s2[i - 1] == s3[i - 1]:
                dp[0][i] = True

        for i in range(1, k):
            for j in range(1, l):
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]

if __name__ == "__main__":
    print Solution().isInterleave("", "", "")
