class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = dict()
        for elt in s:
            d[elt] = d.get(elt, 0) + 1
        for elt in t:
            d[elt] = d.get(elt, 0) - 1
        for k, v in d.items():
            if v in {-1, 1}:
                return k
