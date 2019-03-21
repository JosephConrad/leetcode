from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1, len(s) + 1):
            dp += any( dp[j] and s[j:i] in wordDict for j in range(i) ),
        return dp[-1]




if __name__ == "__main__":
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
