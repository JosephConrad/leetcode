# 151. Reverse Words in a String
#
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# click to show clarification.
#
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.


class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])


class Solution2(object):
    def reverseWords(self, s):
        s = list(reversed(s))
        beg = 0
        for i, c in enumerate(s):
            if c is ' ':
                Solution2.reverse(s, beg, i)
            else:
                beg == i + 1
        return str(s)

    @staticmethod
    def reverse(s, i, j):
        while i <= j:
            s[i], s[j] = s[j], s[i]


if __name__ == '__main__':
    print Solution().reverseWords('python rocks')
    print Solution().reverseWords('python rocks')
