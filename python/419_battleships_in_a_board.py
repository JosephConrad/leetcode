class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        k, l = len(board), len(board[0])
        counter = 0
        for i in range(k):
            for j in range(l):
                if board[i][j] == '.': continue
                if i > 0 and board[i - 1][j] == 'X': continue
                if j > 0 and board[i][j - 1] == 'X': continue
                counter += 1
        return counter


if __name__ == "__main__":
    print Solution().countBattleships([
        ['X', '.', '.', 'X'],
        ['.', 'X', '.', 'X'],
        ['.', '.', '.', 'X']
    ])
    print Solution().countBattleships([
        ['X', '.', '.', 'X']
    ])
    print Solution().countBattleships([
        ['X']
    ])
    print Solution().countBattleships([])
