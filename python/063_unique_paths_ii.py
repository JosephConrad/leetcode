class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            grid[i] = map(lambda x: x * (-1), grid[i])
        print grid
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == -1:
                break
            grid[i][0] = 1
        for i in range(m):

            if grid[0][i] == -1:
                break
            grid[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == -1:
                    continue
                if grid[i - 1][j] == -1 and grid[i][j - 1] == -1:
                    grid[i][j] = -1
                elif grid[i - 1][j] > -1 and grid[i][j - 1] > -1:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1] + 1
        return grid[-1][-1] if grid[-1][-1] > 0 else 0


if __name__ == "__main__":
    print Solution().uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])
    print Solution().uniquePathsWithObstacles([[1]])
