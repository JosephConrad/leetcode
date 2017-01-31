class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            board[i] = list(board[i])
        self.solver(board)

    def solver(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    continue
                for k in range(9):
                    board[i][j] = chr(ord('1') + k)
                    if self.isValid(board, i, j) and self.solver(board):
                        return True
                    board[i][j] = '.'
                return False
        return True

    def isValid(self, board, x, y):
        for i in xrange(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in xrange(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        row = 3 * (x / 3)
        column = 3 * (y / 3)
        for i in range(row, row + 3):
            for j in range(column, column + 3):
                if board[i][j] == board[x][y] and i != x and j != y:
                    return False
        return True


sol = Solution()
board = ["123456789",
         "456789123",
         "789123456",
         "214365897",
         "365897214",
         "897214365",
         "531642978",
         "64.97.53.",
         "97.53.64."]
sol.solveSudoku(board)
print board
board = ["..9748...",
         "7........",
         ".2.1.9...",
         "..7...24.",
         ".64.1.59.",
         ".98...3..",
         "...8.3.2.",
         "........6",
         "...2759.."]
sol.solveSudoku(board)
print board
