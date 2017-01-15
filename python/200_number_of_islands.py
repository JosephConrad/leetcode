class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        self.row = len(grid)
        self.col = len(grid[0])
        used = [[False for j in xrange(self.col)] for i in xrange(self.row)]

        counter = 0
        for r in range(self.row):
            for c in xrange(self.col):
                if grid[r][c] is '1' and used[r][c] is False:
                    counter += 1
                    self.island_dfs(grid, used, r, c)
        return counter

    def island_dfs(self, grid, used, r, c):
        if grid[r][c] == '0' or used[r][c] is True:
            return
        used[r][c] = True

        if r + 1 != self.row:
            self.island_dfs(grid, used, r + 1, c)
        if r != 0:
            self.island_dfs(grid, used, r - 1, c)
        if c + 1 != self.col:
            self.island_dfs(grid, used, r, c + 1)
        if c != 0:
            self.island_dfs(grid, used, r, c - 1)


if __name__ == "__main__":
    print Solution().numIslands(["11110", "11010", "11000", "00000"])
