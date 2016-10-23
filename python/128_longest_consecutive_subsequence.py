__author__ = 'davide'

import itertools


class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def MakeSet(x):
    x.parent = x
    x.rank = 0
    x.size = 1


def Union(x, y):
    x_root = Find(x)
    y_root = Find(y)
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
        x_root.size += y_root.size
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
        y_root.size += x_root.size
    elif x_root != y_root:  # Unless x and y are already in same set, merge them
        y_root.parent = x_root
        x_root.rank += 1
        x_root.size += y_root.size


def Find(x):
    if x.parent == x:
        return x
    else:
        x.parent = Find(x.parent)
        return x.parent


def tree_size(x):
    return x.size


""""""""""""""""""""""""""""""""""""""""""


# sample code using Union-Find (not needed)


def solve(tab):
    used, maks_size = dict(), 0
    nodes = [Node(elt) for elt in tab]
    [MakeSet(node) for node in nodes]
    for node in nodes:
        used[node.value] = node
    for node in nodes:
        if node.value - 1 in used:
            Union(node, used[node.value - 1])
        if node.value + 1 in used:
            Union(node, used[node.value + 1])
    return max(map(tree_size, nodes))


print solve([100, 4, 200, 1, 3, 2])

#
# l = [Node(ch) for ch in "abcdefg"]  # list of seven objects with distinct labels
# print ""
# print "objects labels:\t\t\t", [str(i) for i in l]
#
# [MakeSet(node) for node in l]  # starting with every object in its own set
#
# sets = [str(Find(x)) for x in l]
# print "set representatives:\t\t", sets
# print "number of disjoint sets:\t", len([i for i in itertools.groupby(sets)])
#
# assert (Find(l[0]) != Find(l[2]))
# Union(l[0], l[2])  # joining first and third
# assert (Find(l[0]) == Find(l[2]))
#
# assert (Find(l[0]) != Find(l[1]))
# assert (Find(l[2]) != Find(l[1]))
# Union(l[0], l[1])  # joining first and second
# assert (Find(l[0]) == Find(l[1]))
# assert (Find(l[2]) == Find(l[1]))
#
# Union(l[-2], l[-1])  # joining last two sets
# Union(l[-3], l[-1])  # joining last two sets
#
# sets = [str(Find(x)) for x in l]
# print "set representatives:\t\t", sets
# print "number of disjoint sets:\t", len([i for i in itertools.groupby(sets)])
#
# for o in l:
#     del o.parent

# print(u)
# u.union(0, 3)
# print(u)
# print(u.find(0))
# print(u.find(3))

# u = UnionFind(10)
# adj_list = []
#
#
# def dfs(v, visited):
#     visited.append(v)
#
#     for n in adj_list[v]:
#         if n not in visited:
#             dfs(n, visited)
#
#
# dfs(4, [])
#
#
#
#
# tab = [2,1,5,6,2,3]
# stack = Stack()
# stack.push((0, tab[0]))
# i = 1
# while i < len(tab):
#     if :
#         index, top = stack.peek()
#         if tab[i] > top:
#             stack.push((i, tab[i]))
#
#
