class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for elt in s:
            d[elt] = d[elt] + 1 if elt in d else  1
        odd = False
        result = 0
        for key, value in d.iteritems():
            result += value - value % 2
            if value % 2 == 1:
                odd = True
        return result + 1 if odd else result


if __name__ == "__main__":
    print Solution().longestPalindrome("abccccdd")
