# 5. Longest Palindromic Substring   QuestionEditorial Solution  My Submissions
#
# Given a string S, find the longest palindromic substring in S. You may assume
#   that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


def odd(string, k, n):
    l = k - 1
    p = k + 1
    while l >= 0 and p < n and string[l] is string[p]:
        l -= 1
        p += 1
    return string[l: p + 1]


def even(string, k, n):
    l = k
    p = k + 1
    while l >= 0 and p < n and string[l] is string[p]:
        l -= 1
        p += 1
    return string[l: p + 1]


def update_longest(maks, word):
    return word if len(word) > maks else maks


def pal(string):
    n = len(string)
    maks = string[0]
    for i in range(n):
        word = odd(string, i, n)
        maks = update_longest(maks, word)
        word = even(string, i, n)
        maks = update_longest(maks, word)
    return maks


print 'a'

print pal("AAABCBAABB")
