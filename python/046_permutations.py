def all_permutations(permutation, letters):
    new_perms = [permutation + letter for letter in letters]
    for new_perm in new_perms:
        print new_perm
        all_permutations(new_perm, set(letters) - set(list(new_perm)))


all_permutations("", ['A', 'B', 'C', 'D'])


def all_perms(permutation, letters):
    acc = []
    new_perms = [permutation + letter for letter in letters]
    for new_perm in new_perms:
        acc.append(new_perm)
        acc += all_perms(new_perm, set(letters) - set(list(new_perm)))
    return acc


print all_perms("", ['A', 'B', 'C'])


def all_perm(P, l=0):
    if l == len(P):
        print P
    for i in range(l, len(P)):
        P[i], P[l] = P[l], P[i]
        all_perm(P, l + 1)
        P[l], P[i] = P[i], P[l]


all_perm(['A', 'B'])
all_perm(['A', 'B', 'C'])
all_perm(['A', 'B', 'C', 'D'])
