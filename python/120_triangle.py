# 120. Triangle
#
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        self.triangle = triangle
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(self.get_elt(i - 1, j), self.get_elt(i - 1, j - 1))
        return min(triangle[-1])

    def get_elt(self, i, j):
        if not 0 <= j < len(self.triangle[i]):
            return 10000
        return self.triangle[i][j]


if __name__ == "__main__":
    print Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])
    print Solution().minimumTotal([])

