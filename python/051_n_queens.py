def under_attack(board, row, col):
    for i, j in enumerate(board):
        if row == i: return True
        if col == j: return True
        if abs(row - i) == abs(col - j): return True
    return False


def n_queens(board, i, n, acc):
    if i == n:
        acc.append(board)
    for j in range(n):
        if not under_attack(board, i, j):
            n_queens(board + [j], i + 1, n, acc)
    return acc

print n_queens([], 0, 4, [])
