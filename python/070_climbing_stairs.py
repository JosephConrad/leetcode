# 70. Climbing Stairs   QuestionEditorial Solution  My Submissions

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways
#       can you climb to the top?


def make_set(x):
    x.parent = None


def find(x):
    if x.parent is None:
        return x
    return find(x.parent)


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        x_root.parent = y_root


adj_list = []


def dfs(v, visited):
    visited.append(v)

    for n in adj_list[v]:
        if n not in visited:
            dfs(n, visited)


dfs(4, [])
