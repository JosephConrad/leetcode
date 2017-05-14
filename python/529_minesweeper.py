class Solution(object):
    def __init__(self):
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click[0], click[1]
        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return
        if board[x][y] == 'M':
            board[x][y] = 'X'
        if board[x][y] == 'E':
            n = self.bombs(x, y, board)
            board[x][y] = str(n or 'B')
            for dx, dy in self.moves * (not n):
                self.updateBoard(board, [x + dx, y + dy])
        return board

    def bombs(self, x, y, B):
        bombs = [B[x + dx][y + dy] == 'M' for dx, dy in self.moves if 0 <= x + dx < len(B) and 0 <= y + dy < len(B[0])]
        return sum(bombs)


if __name__ == "__main__":
    print Solution().updateBoard(board=[['E', 'E', 'E', 'E', 'E'],
                                        ['E', 'E', 'M', 'E', 'E'],
                                        ['E', 'E', 'E', 'E', 'E'],
                                        ['E', 'E', 'E', 'E', 'E']],
                                 click=[0, 0])
    print Solution().updateBoard(board=[['B', '1', 'E', '1', 'B'],
                                        ['B', '1', 'M', '1', 'B'],
                                        ['B', '1', '1', '1', 'B'],
                                        ['B', 'B', 'B', 'B', 'B']],
                                 click=[1, 2])
