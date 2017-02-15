class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        m, n = len(board), len(board[0])
        save = [(i, j) for i in range(m) for j in range(n) if i in {0, m - 1} or j in {0, n - 1}]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]


if __name__ == "__main__":
    # Your MedianFinder object will be instantiated and called as such:
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    print board

    board = [
        ['X', 'X'],
        ['X', 'O']
    ]
    Solution().solve(board)
    print board
