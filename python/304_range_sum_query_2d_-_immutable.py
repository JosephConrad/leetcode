class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j] += self.a(i - 1, j) + self.a(i, j - 1) - self.a(i - 1, j - 1)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.a(row2, col2) - self.a(row1 - 1, col2) - self.a(row2, col1 - 1) + self.a(row1 - 1,
                                                                                             col1 - 1)

    def a(self, i, j):
        return self.dp[i][j] if i >= 0 and j >= 0 else 0


# Your NumMatrix object will be instantiated and called as such:


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    print NumMatrix(matrix).sumRegion(2, 1, 4, 3)
    matrix = [[]]
