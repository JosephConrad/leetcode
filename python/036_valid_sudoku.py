def is_valid(numbers):
    numbers = map(int, list(filter(lambda x: x is not '.', list(numbers))))
    return sum(set(numbers)) == sum(numbers)


def check(solutions):
    for solution in solutions:
        if not is_valid(solution):
            return False
    return True


class Solution(object):
    def isValidSudoku(self, board):
        squares = []
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                square = []
                for i in range(row, row + 3):
                    for j in range(column, column + 3):
                        square.append(board[i][j])
                squares.append(square)
        vertical = board
        horizontal = list(zip(*board))

        return check(horizontal) and check(squares) and check(vertical)


sol = Solution()
print sol.isValidSudoku(["..4...63.",
                         ".........",
                         "5......9.",
                         "...56....",
                         "4.3.....1",
                         "...7.....",
                         "...5.....",
                         ".........",
                         "........."])

print sol.isValidSudoku([".87654321",
                         "2........",
                         "3........",
                         "4........",
                         "5........",
                         "6........",
                         "7........",
                         "8........",
                         "9........"])


