from sys import maxint


def value(tab, i, n, guard=-maxint):
    if i in {-1, n}:
        return guard
    return tab[i]


def find_local_mins(tab):
    local_mins = []
    n = len(tab)

    for i in range(n):
        left = value(tab, i - 1, n, maxint)
        middle = value(tab, i, n, maxint)
        right = value(tab, i + 1, n, maxint)
        if left > middle < right:
            local_mins.append(i)

    return local_mins


print find_local_mins([6, 5, 0, 1, 9, 3, 4, 5, 6, 4, 1])


def min_candies(tab, local_mins):
    max_index


def candies(tab):
    local_mins = find_local_mins(tab)
    return min_candies(tab, local_mins)
