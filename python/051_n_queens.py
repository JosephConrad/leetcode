# 51. N-Queens
#
# The n-queens puzzle is the problem of placing n queens on an n×n
#   chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
#   both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution(object):
    def solveNQueens(self, n):
        return map(lambda conf: self.print_board(conf), self.n_queens([], 0, n, []))

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

    def print_board(self, conf):
        result = []
        for queen in conf:
            row = ['.'] * len(conf)
            row[queen] = 'Q'
            result.append(''.join(row))
        return result


if __name__ == "__main__":
    print Solution().totalNQueens(4)
