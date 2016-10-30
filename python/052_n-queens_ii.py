# 52. N-Queens II
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    def totalNQueens(self, n):
        return len(self.n_queens([], 0, n, []))

    def under_attack(self, board, row, col):
        for i, j in enumerate(board):
            if row == i: return True
            if col == j: return True
            if abs(row - i) == abs(col - j): return True
        return False

    def n_queens(self, board, i, n, acc):
        if i == n:
            acc.append(board)
        for j in range(n):
            if not self.under_attack(board, i, j):
                self.n_queens(board + [j], i + 1, n, acc)
        return acc


if __name__ == "__main__":
    print Solution().totalNQueens(8)
