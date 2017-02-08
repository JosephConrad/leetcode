# can be more tricky to use only one row table:
#   https://discuss.leetcode.com/topic/7024/sharing-my-solution-with-o-n-space-o-mn-runtime


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0

        k, l = len(dungeon), len(dungeon[0])

        dp = [[0 for _ in range(l)] for _ in range(k)]

        dp[k - 1][l - 1] = max(1, 1 - dungeon[k - 1][l - 1])

        for i in reversed(range(l - 1)):
            dp[k - 1][i] = max(1, dp[k - 1][i + 1] - dungeon[k - 1][i])

        for i in reversed(range(k - 1)):
            dp[i][l - 1] = max(1, dp[i + 1][l - 1] - dungeon[i][l - 1])

        for i in reversed(range(k - 1)):
            for j in reversed(range(l - 1)):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0]


if __name__ == "__main__":
    print Solution().calculateMinimumHP([])
    print Solution().calculateMinimumHP([[0]])
    print Solution().calculateMinimumHP([
        [1, -2, 3],
        [2, -2, -2]
    ])
    print Solution().calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ])
