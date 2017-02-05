class Solution(object):
    def longestIncreasingPath(self, nums):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not nums:
            return 0
        self.k, self.l = len(nums), len(nums[0])
        self.visited = [[0 for _ in range(self.l)] for _ in range(self.k)]
        longest_path = 0
        for i in range(self.k):
            for j in range(self.l):
                longest_path = max(longest_path, self.longestPath(i, j, nums))
        return longest_path

    def longestPath(self, i, j, nums):
        if self.visited[i][j]:
            return self.visited[i][j]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        longest_path = 0
        for d in directions:
            x, y = i + d[0], j + d[1]
            longest_path = max(longest_path, self.longestPath(x, y, nums) if self.canMove(x, y, i, j, nums) else 0)

        self.visited[i][j] = longest_path + 1
        return self.visited[i][j]

    def canMove(self, i, j, old_i, old_j, nums):
        return self.isOnBoard(i, j) and nums[i][j] > nums[old_i][old_j]

    def isOnBoard(self, i, j):
        if i < 0 or i >= self.k:
            return False
        if j < 0 or j >= self.l:
            return False
        return True


if __name__ == "__main__":
    print Solution().longestIncreasingPath(nums=[[1, 2]])
    print Solution().longestIncreasingPath(nums=[
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ])
    print Solution().longestIncreasingPath(nums=[
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ])


    # def longestPath1(self, i, j, nums):
    #     if self.visited[i][j]:
    #         return self.visited[i][j]
    #
    #     l = self.longestPath(i - 1, j, nums) if self.canMove(i - 1, j, i, j, nums) else 0
    #     r = self.longestPath(i + 1, j, nums) if self.canMove(i + 1, j, i, j, nums) else 0
    #     u = self.longestPath(i, j + 1, nums) if self.canMove(i, j + 1, i, j, nums) else 0
    #     d = self.longestPath(i, j - 1, nums) if self.canMove(i, j - 1, i, j, nums) else 0
    #
    #     longest_path = max(l, r, u, d) + 1
    #     self.visited[i][j] = longest_path
    #     return longest_path
