class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == '0':
            return 0

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[-1] = 1

        for i in range(1, len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i - 1]
            if self.is_valid(s[i - 1:i + 1]):
                dp[i] += dp[i - 2]
        return dp[len(s) - 1]

    def is_valid(self, ending):
        if ending[0] == '0':
            return False
        ending = int(ending)
        if 1 <= ending <= 26:
            return True

if __name__ == "__main__":
    print Solution().numDecodings("101")
    print Solution().numDecodings("12")
    print Solution().numDecodings("121")
    print Solution().numDecodings("121234123231232321")
