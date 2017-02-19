# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            s = (i + j)/ 2
            if guess(s) == 0:
                return s
            elif guess(s) == -1:
                j = s - 1
            elif guess(s) == 1:
                i = s + 1